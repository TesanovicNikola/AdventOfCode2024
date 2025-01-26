from typing import List

class PrintQueue:
    """Handles operations for processing and validating vector rules."""

    def __init__(self, filename: str):
        """
        Initializes the PrintQueue with a filename to read rules from.

        Args:
            filename: Path to the input file containing rules.
        """
        self.filename = filename
        self.pairs = []
        self.vectors = []

    def read_rules(self) -> None:
        """
        Reads rules from the file and populates pairs and vectors attributes.
        """
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

    def get_invalid_vectors(self) -> List[List[int]]:
        """
        Validates vectors based on pair constraints and returns the invalid vectors.

        Returns:
            A list of vectors that violate pair constraints.
        """
        invalid = []
        for vector in self.vectors:
            is_valid = True
            for a, b in self.pairs:
                if a in vector and b in vector:
                    idx_a = vector.index(a)
                    idx_b = vector.index(b)
                    if idx_a > idx_b:
                        is_valid = False
                        break
            if not is_valid:
                invalid.append(vector)
        return invalid

    def fix_invalid_vectors(self, invalid_vectors: List[List[int]]) -> List[List[int]]:
        """
        Fixes invalid vectors by enforcing pair rules and numerical order.

        Args:
            invalid_vectors: A list of vectors that violate pair constraints.

        Returns:
            A list of corrected vectors.
        """
        def process_vector(vector: List[int]) -> List[int]:
            # Create adjacency list for required ordering
            graph = {num: set() for num in vector}
            for a, b in self.pairs:
                if a in graph and b in graph:
                    graph[a].add(b)  # b must come after a

            # Kahn's algorithm for topological sort
            in_degree = {u: 0 for u in graph}
            for u in graph:
                for v in graph[u]:
                    in_degree[v] += 1

            queue = [u for u in in_degree if in_degree[u] == 0]
            result = []

            while queue:
                # Sort queue descending to maximize numerical order where possible
                queue.sort(reverse=True)
                u = queue.pop(0)
                result.append(u)
                for v in graph[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)

            return result if len(result) == len(vector) else vector

        return [process_vector(vec) for vec in invalid_vectors]

    @staticmethod
    def sum_middle_elements(valid_vectors: List[List[int]]) -> int:
        """
        Calculates the sum of the middle elements from all valid vectors.

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
    invalid_vectors = queue.get_invalid_vectors()
    fixed_vectors = queue.fix_invalid_vectors(invalid_vectors)
    print("Sum of middle elements:", queue.sum_middle_elements(fixed_vectors))
    print("Valid vectors:", fixed_vectors)