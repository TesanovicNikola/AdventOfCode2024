def load_data(file_path: str) -> list:
    """Loads data from a file and splits it into a list of lines.

    Args:
        file_path: A string representing the path to the input file.

    Returns:
        A list of strings, each representing a line from the file.
    """
    with open(file_path, "r") as file:
        data = file.read().strip()
        return data.splitlines()


def count_mas_word(data: list) -> int:
    """Counts the occurrences of the word 'MAS' (and its reverse) diagonally.

    Args:
        data: A list of strings representing the input grid.

    Returns:
        An integer representing the number of matches found.
    """
    rows = len(data)
    cols = len(data[0])
    hit_count = 0

    word = ["M", "A", "S"]
    reverse_word = word[::-1]

    for y in range(rows - 2):
        for x in range(cols - 2):
            # Extract characters for both diagonals
            diagonal1 = [data[y][x], data[y + 1][x + 1], data[y + 2][x + 2]]
            diagonal2 = [data[y + 2][x], data[y + 1][x + 1], data[y][x + 2]]

            # Check if both diagonals match target or reverse target
            if (diagonal1 == word or diagonal1 == reverse_word) and (diagonal2 == word or diagonal2 == reverse_word):
                hit_count += 1

    return hit_count


def main():
    """Main function to load data, process it, and print the result."""
    data_input = load_data("input.txt")
    result = count_mas_word(data_input)
    print(result)


if __name__ == "__main__":
    main()
