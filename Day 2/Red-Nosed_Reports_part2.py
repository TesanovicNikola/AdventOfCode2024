def is_valid_sequence(seq):
    #Raste
    if all(seq[i] <= seq[i + 1] for i in range(len(seq) - 1)):
        return all(1 <= seq[i + 1] - seq[i] <= 3 for i in range(len(seq) - 1))
    #Opada
    elif all(seq[i] >= seq[i + 1] for i in range(len(seq) - 1)):
        return all(1 <= seq[i] - seq[i + 1] <= 3 for i in range(len(seq) - 1))
    return False


def is_safe(sequence):
    #Koji su tacni bez menjanja
    if is_valid_sequence(sequence):
        return True
    #Brute force, pokusaj svaku mogucu kombinaciju
    for i in range(len(sequence)):
        temp_seq = sequence[:i] + sequence[i + 1:]  # Remove one element
        if is_valid_sequence(temp_seq):
            return True
    #Ako nema ni jedna da je true, onda vracaj False
    return False


# Test cases
with open('input.txt', 'r') as file:
    lines = file.readlines()

data = [list(map(int, line.split())) for line in lines]
safe_counter = 0
for seq in data:
    if is_safe(seq):
        safe_counter += 1
print(safe_counter)

