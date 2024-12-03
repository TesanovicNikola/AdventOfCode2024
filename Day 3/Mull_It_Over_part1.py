import re
import pandas as pd

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def string_match(text):
    regex = r"mul\((\d+),(\d+)\)"
    return re.findall(regex, text)


file_name = 'input.txt'
data = load_data(file_name)
data = string_match(data)

total_sum = 0
for i in range(len(data)):
    temp_vec = pd.DataFrame({"Column1": data[i]}, dtype=int)
    total_sum += temp_vec.iloc[0]*temp_vec.iloc[1]

print(total_sum)
