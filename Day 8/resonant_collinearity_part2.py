import math
from collections import defaultdict


class ResonantCollinearity:
    """Class to process an input grid and compute collinear resonance points."""

    def __init__(self, filename: str):
        """Initializes the grid by reading from the given input file."""
        self.grid = self._read_file(filename)
        self.height = len(self.grid)
        self.width = len(self.grid[0]) if self.height > 0 else 0
        self.antennas = self._collect_antennas()
        self.antinodes = set()

    @staticmethod
    def _read_file(filename: str) -> list[str]:
        """Reads the input file and returns its content as a list of strings.

        Args:
            filename: The path to the input file.

        Returns:
            A list of strings, where each string represents a line from the file.
        """
        with open(filename, "r") as file:
            return [line.strip() for line in file]

    def _collect_antennas(self):
        """Collects antenna positions grouped by frequency from the grid."""
        antennas = defaultdict(list)
        for y, line in enumerate(self.grid):
            for x, c in enumerate(line):
                if c != '.':
                    antennas[c].append((x, y))
        return antennas

    def _process_frequency(self, points):
        """Processes a single frequency's antenna positions to find collinear points."""
        if len(points) < 2:
            return

        for i, a in enumerate(points):
            for j in range(i + 1, len(points)):
                b = points[j]
                dx, dy = b[0] - a[0], b[1] - a[1]
                if dx == 0 and dy == 0:
                    continue

                gcd_val = math.gcd(abs(dx), abs(dy))
                step_x, step_y = dx // gcd_val, dy // gcd_val

                self._generate_points(a, step_x, step_y)
                self._generate_points(a, -step_x, -step_y)

    def _generate_points(self, start, step_x, step_y):
        """Generates collinear points in a given direction and adds them to antinodes."""
        x, y = start
        while 0 <= x < self.width and 0 <= y < self.height:
            self.antinodes.add((x, y))
            x += step_x
            y += step_y

    def compute_antinodes(self):
        """Computes all collinear resonance points."""
        for freq, points in self.antennas.items():
            self._process_frequency(points)
        return len(self.antinodes)


if __name__ == "__main__":
    rc = ResonantCollinearity('input.txt')
    print(rc.compute_antinodes())