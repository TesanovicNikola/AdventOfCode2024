class GuardGallivant:
    def __init__(self, filename: str):
        """
        Initializes the GuardGallivant with a filename to read rules from.

        Args:
            filename: Path to the input file containing the map.
        """
        self.filename = filename
        self.map_data = []

    def read_file(self) -> None:
        """
        Reads the map data from the file and stores it in the instance.
        """
        with open(self.filename, 'r') as file:
            self.map_data = [line.strip() for line in file]

    def find_start(self) -> tuple[int, int]:
        """
        Finds the starting position (marked as '^') in the map.

        Returns:
            A tuple (x, y) representing the starting coordinates.

        Raises:
            ValueError: If the starting position '^' is not found in the map.
        """
        for y, row in enumerate(self.map_data):
            for x, cell in enumerate(row):
                if cell == '^':
                    return x, y
        raise ValueError("Guard not found in the map.")

    def calculate_unique_steps(self) -> int:
        """
        Calculates the number of unique steps the guard can take before being
        blocked or going out of bounds.

        Returns:
            The number of unique positions visited by the guard.
        """
        start_x, start_y = self.find_start()
        rows = len(self.map_data)
        cols = len(self.map_data[0]) if rows > 0 else 0

        # Convert map to mutable list of lists and update the starting position
        map_data = [list(row) for row in self.map_data]
        map_data[start_y][start_x] = '.'
        visited = set()
        visited.add((start_x, start_y))

        # Directions: up, right, down, left (dx, dy)
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        current_dir = 0  # starts facing up
        current_x, current_y = start_x, start_y

        while True:
            dx, dy = directions[current_dir]
            while True:
                next_x = current_x + dx
                next_y = current_y + dy
                # Check if next step is out of bounds
                if not (0 <= next_x < cols and 0 <= next_y < rows):
                    return len(visited)
                # Check if next cell is an obstacle
                if map_data[next_y][next_x] == '#':
                    break
                # Move to the next cell
                current_x, current_y = next_x, next_y
                visited.add((current_x, current_y))
            # Change direction clockwise
            current_dir = (current_dir + 1) % 4


# Example usage
if __name__ == "__main__":
    map_field = GuardGallivant("input.txt")
    map_field.read_file()
    unique_steps = map_field.calculate_unique_steps()
    print(f"Unique steps the guard can take: {unique_steps}")

