from typing import List

class PrintQueue:
    """Handles operations for processing and validating vector rules."""

    def __init__(self, filename: str):
        """Initializes the PrintQueue with a filename to read rules from.

        Args:
            filename: Path to the input file containing rules.
        """
        self.filename = filename
        self.pairs = []
        self.vectors = []

    def read_rules(self) -> None:
        """Reads rules from the file and populates pairs and vectors attributes."""
        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                stripped_line = line.strip()
                if not stripped_line:
                    continue  # Skip empty lines

                if "|" in stripped_line:
                    # Process pairs separated by "|"
                    parts = stripped_line.split("|")
                    if len(parts) != 2:
                        continue  # Skip invalid pair formats
                    try:
                        num1, num2 = map(int, parts)
                        self.pairs.append([num1, num2])
                    except ValueError:
                        pass  # Skip lines with non-integer values

                elif "," in stripped_line:
                    # Process vectors separated by ","
                    parts = stripped_line.split(",")
                    try:
                        vector = list(map(int, parts))
                        self.vectors.append(vector)
                    except ValueError:
                        pass  # Skip lines with non-integer values

    def get_valid_vectors(self) -> List[List[int]]:
        """Validates vectors based on pair constraints and returns the valid vectors.

        Returns:
            A list of vectors that meet all pair constraints.
        """
        valid = []
        for vector in self.vectors:
            is_valid = True
            for a, b in self.pairs:
                if a in vector and b in vector:
                    idx_a = vector.index(a)
                    idx_b = vector.index(b)
                    if idx_a > idx_b:
                        is_valid = False
                        break
            if is_valid:
                valid.append(vector)
        return valid

    @staticmethod
    def sum_middle_elements(valid_vectors: List[List[int]]) -> int:
        """Calculates the sum of the middle elements from all valid vectors.

        Args:
            valid_vectors: A list of valid vectors (lists of integers).

        Returns:
            The total sum of the middle elements across all valid vectors.
        """
        total = 0
        for vector in valid_vectors:
            if not vector:
                continue
            length = len(vector)
            middle_idx = (length + 1) // 2 - 1  # Adjusted formula for middle index
            total += vector[middle_idx]
        return total

# Example usage
if __name__ == "__main__":
    queue = PrintQueue("input.txt")
    queue.read_rules()
    valid_vectors = queue.get_valid_vectors()
    print("Sum of middle elements:", queue.sum_middle_elements(valid_vectors))
    print("Valid vectors:", valid_vectors)
