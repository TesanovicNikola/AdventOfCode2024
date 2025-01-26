class GuardGallivant:
    """Simulates a guard's movement on a map and detects infinite loops."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.map_data = self.read_map(file_path)
        self.start_x, self.start_y = self.find_start(self.map_data)
        self.original_map = [
            row[:self.start_x] + '.' + row[self.start_x+1:]
            if y == self.start_y else row
            for y, row in enumerate(self.map_data)
        ]

    @staticmethod
    def read_map(file_path):
        """Reads the map data from a file."""
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

    @staticmethod
    def find_start(map_data):
        """Finds the guard's starting position (^)."""
        for y, row in enumerate(map_data):
            for x, char in enumerate(row):
                if char == '^':
                    return x, y
        raise ValueError("Guard not found in the map.")

    def is_infinite_loop(self, add_x, add_y):
        """Checks if adding an obstacle at (add_x, add_y) causes an infinite loop."""
        if self.original_map[add_y][add_x] != '.':
            return False

        # Create a temporary map with the obstacle
        temp_map = [list(row) for row in self.original_map]
        temp_map[add_y][add_x] = '#'
        temp_map = [''.join(row) for row in temp_map]

        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left
        current_dir = 0
        current_x, current_y = self.start_x, self.start_y
        visited_states = set()

        while True:
            state = (current_x, current_y, current_dir)
            if state in visited_states:
                return True  # Cycle detected
            visited_states.add(state)

            dx, dy = directions[current_dir]
            next_x = current_x + dx
            next_y = current_y + dy

            # Check bounds
            if not (0 <= next_x < len(temp_map[0]) and 0 <= next_y < len(temp_map)):
                return False  # Guard escaped

            if temp_map[next_y][next_x] == '#':
                current_dir = (current_dir + 1) % 4  # Rotate clockwise
            else:
                current_x, current_y = next_x, next_y

    def count_infinite_loop_positions(self):
        """Counts positions where adding an obstacle causes an infinite loop."""
        count = 0
        for y in range(len(self.original_map)):
            for x in range(len(self.original_map[0])):
                if self.original_map[y][x] == '.':
                    if self.is_infinite_loop(x, y):
                        count += 1
        return count


if __name__ == "__main__":
    guard_gallivant = GuardGallivant('input.txt')
    print(guard_gallivant.count_infinite_loop_positions())