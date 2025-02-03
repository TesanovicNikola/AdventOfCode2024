from collections import defaultdict


class ResonantCollinearity:
    """Class to compute resonant collinearity from an input grid."""

    def __init__(self, filename: str):
        """Initializes the class by reading the input grid from a file.

        Args:
            filename (str): Path to the input file.
        """
        self.filename = filename
        self.lines = self._read_file()
        self.height = len(self.lines)
        self.width = len(self.lines[0]) if self.height > 0 else 0
        self.antennas = self._collect_antennas()

    def _read_file(self):
        """Reads the input file and returns the grid lines.

        Returns:
            list: A list of strings representing the grid.
        """
        with open(self.filename, 'r') as file:
            return [line.strip() for line in file]

    def _collect_antennas(self):
        """Collects antennas from the grid grouped by frequency.

        Returns:
            dict: A dictionary mapping frequencies to their positions.
        """
        antennas = defaultdict(list)
        for y, line in enumerate(self.lines):
            for x, c in enumerate(line):
                if c != '.':
                    antennas[c].append((x, y))
        return antennas

    def compute_antinodes(self):
        """Computes the set of unique antinodes.

        Returns:
            int: The number of unique antinodes.
        """
        antinodes = set()

        for freq, points in self.antennas.items():
            n = len(points)
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = points[i], points[j]
                    dx, dy = b[0] - a[0], b[1] - a[1]

                    # Compute anti node positions
                    p1 = (b[0] + dx, b[1] + dy)
                    p2 = (a[0] - dx, a[1] - dy)

                    if 0 <= p1[0] < self.width and 0 <= p1[1] < self.height:
                        antinodes.add(p1)
                    if 0 <= p2[0] < self.width and 0 <= p2[1] < self.height:
                        antinodes.add(p2)

        return len(antinodes)


if __name__ == "__main__":
    collinearity = ResonantCollinearity('input.txt')
    print(collinearity.compute_antinodes())