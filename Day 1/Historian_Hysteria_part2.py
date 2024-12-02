import pandas as pd

file_name = 'input.txt'

list1, list2 = [], []

with open(file_name, 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

df1 = pd.DataFrame({"Column1": list1}, dtype="int")
df2 = pd.DataFrame({"Column2": list2}, dtype="int")

total_sum = 0
for i in range(len(df1)):
    count = (df2 == df1.iloc[i].values).sum().sum()
    total_sum += df1.iloc[i].values * count

print(total_sum)