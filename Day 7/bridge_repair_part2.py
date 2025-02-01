class BridgeRepair:
    """A class for processing bridge repair data from a file."""

    def __init__(self, filename: str):
        """Initializes BridgeRepair with a filename.

        Args:
            filename (str): The name of the input file.
        """
        self.filename = filename
        self.data_vector = []
        self.target_value = []
        self.right_sums = 0

    @staticmethod
    def can_reach_result_value(data_value, result_value):
        """Determines whether the result_value can be reached using given numbers.

        Args:
            data_value (list[int]): A list of integers.
            result_value (int): The target result value.

        Returns:
            bool: True if the result_value can be reached, False otherwise.
        """
        possible = {data_value[0]}
        for num in data_value[1:]:
            next_possible = set()
            for val in possible:
                next_possible.add(val + num)
                next_possible.add(val * num)
                concatenated = int(str(val) + str(num))
                next_possible.add(concatenated)
            possible = next_possible
        return result_value in possible

    def read_file(self) -> None:
        """Reads the input file and processes each line."""
        with open(self.filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                result_row, data_row = line.split(':')
                result_val = int(result_row)
                data_val = list(map(int, data_row.split()))
                if self.can_reach_result_value(data_val, result_val):
                    self.right_sums += result_val


if __name__ == "__main__":
    bridge_repair = BridgeRepair("input.txt")
    bridge_repair.read_file()
    print(bridge_repair.right_sums)