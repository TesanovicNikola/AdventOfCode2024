import pandas as pd

with open('input.txt', 'r') as file:
    lines = file.readlines()

data = [list(map(int, line.split())) for line in lines]
safe_counter = 0

for i in range(len(data)):
    temp_df = pd.DataFrame({'Column1': data[i]}, dtype=int)
    temp_dt_len = len(temp_df)

    if temp_df.iloc[0, 0] < temp_df.iloc[1, 0]:
        hit = True
        j = 0
        while hit and j < (temp_dt_len - 1):
            if (temp_df.iloc[j, 0] < temp_df.iloc[j + 1, 0]) and \
                    ((temp_df.iloc[j + 1, 0] - temp_df.iloc[j, 0]) < 4):
                j += 1
            else:
                hit = False

        if hit:
            safe_counter += 1

    elif temp_df.iloc[0, 0] > temp_df.iloc[1, 0]:
        hit = True
        j = 0
        while hit and j < (temp_dt_len - 1):
            if (temp_df.iloc[j, 0] > temp_df.iloc[j + 1, 0]) and \
                    ((temp_df.iloc[j, 0] - temp_df.iloc[j + 1, 0]) < 4):
                j += 1
            else:
                hit = False

        if hit:
            safe_counter += 1

print(safe_counter)
