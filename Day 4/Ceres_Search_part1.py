def load_data(file_path: str) -> list:
    """Loads data from a file and returns a list of strings, each representing a line in the file.

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[str]: A list of lines from the file, with trailing whitespace removed.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def count_word_in_grid(grid: list, word: str) -> int:
    """Counts occurrences of a word in a 2D grid in all possible directions.

    Args:
        grid (List[str]): A list of strings representing the grid.
        word (str): The word to search for in the grid.

    Returns:
        int: The total number of occurrences of the word in the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (1, 1),  # Diagonal down-right
        (1, -1), # Diagonal down-left
        (0, -1), # Left
        (-1, 0), # Up
        (-1, -1), # Diagonal up-left
        (-1, 1)  # Diagonal up-right
    ]

    def is_valid(x: int, y: int) -> bool:
        """Checks if a given position is within the grid bounds.

        Args:
            x (int): The row index.
            y (int): The column index.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        return 0 <= x < rows and 0 <= y < cols

    def check_direction(x: int, y: int, dx: int, dy: int) -> bool:
        """Checks if the word exists starting from a position in a given direction.

        Args:
            x (int): The starting row index.
            y (int): The starting column index.
            dx (int): The row direction increment.
            dy (int): The column direction increment.

        Returns:
            bool: True if the word is found, False otherwise.
        """
        for k in range(word_len):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True

    hits = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_direction(x, y, dx, dy):
                    hits += 1
    return hits

if __name__ == "__main__":
    grid = load_data('input.txt')

    target_word = "XMAS"
    count = count_word_in_grid(grid, target_word)

    print(count)
