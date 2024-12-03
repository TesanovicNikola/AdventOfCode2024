import re
import pandas as pd


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def string_match(text):
    # Do or Don't regex:
    blocks = re.split(r"don't\(\)|do\(\)", text)
    block_flag = re.findall(r"don't\(\)|do\(\)", text)

    switch_on_off = True
    valid_part = []

    for i, block in enumerate(blocks):
        if switch_on_off:
            valid_part.append(block)
        if i < len(block_flag):
            switch_on_off = block_flag[i] == 'do()'

    valid_text = ''.join(valid_part)

    regex = r"mul\((\d+),(\d+)\)"
    return re.findall(regex, valid_text)


file_name = 'input.txt'
data = load_data(file_name)
data = string_match(data)

total_sum = 0
for i in range(len(data)):
    temp_vec = pd.DataFrame({"Column1": data[i]}, dtype=int)
    total_sum += temp_vec.iloc[0]*temp_vec.iloc[1]

print(total_sum)