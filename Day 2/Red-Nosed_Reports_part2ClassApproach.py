class SequenceValidator:
    def __init__(self, file_path):
        """
        Initialize with the file path.
        :param file_path: path of the input file.
        """
        self.file_path = file_path
        self.data = []
        self.safe_counter = 0

    @staticmethod
    def is_valid_sequence(seq):
        """
        Checks if the sequence is valid ascending or descending.
        :param seq: list of integers
        :return: True if it's valid and False if it's not.
        """
        #Ascending
        if all(seq[i] <= seq[i + 1] for i in range(len(seq) - 1)):
            return all(1 <= seq[i + 1] - seq[i] <= 3 for i in range(len(seq) - 1))
        #Descending
        elif all(seq[i] >= seq[i + 1] for i in range(len(seq) - 1)):
            return all(1 <= seq[i] - seq[i + 1] <= 3 for i in range(len(seq) - 1))
        #Not Asc or Desc, return False
        else:
            return False

    @staticmethod
    def is_safe(sequence):
        """
        Checks if the sequence is safe or not, and brute force checking each combination.
        :param sequence: List of integers
        :return: True if it's valid, False if it's not
        """
        #Case when it checks if it's just increasing or decreasing without doing anything
        if SequenceValidator.is_valid_sequence(sequence):
            return True

        #Remove one and try the sequence for each possible combination until it is True, else False
        for i in range(len(sequence)):
            #Slice one element out
            temp_seq = sequence[:i] + sequence[i + 1:]
            if SequenceValidator.is_valid_sequence(temp_seq):
                return True

        #If no valid sequence was found
        return False

    def load_data(self):
        """
        Load the data of the sequence from the given input .txt file
        """
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        self.data = [list(map(int, line.split())) for line in lines]

    def count_safe_sequences(self):
        """"
        Counts the total number of safe sequences
        :return: Number of total safe sequences
        """
        self.safe_counter = sum(1 for seq in self.data if self.is_safe(seq))
        return self.safe_counter

if __name__ == "__main__":
    #File path
    Validator = SequenceValidator('input.txt')
    #Load the data
    Validator.load_data()
    safe_count = Validator.count_safe_sequences()

    print(safe_count)
