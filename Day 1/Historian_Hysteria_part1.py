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

df1 = df1.sort_values(by="Column1", ascending=True).reset_index(drop=True)
df2 = df2.sort_values(by="Column2", ascending=True).reset_index(drop=True)

distance_df = pd.DataFrame({"Distance": abs(df1["Column1"] - df2["Column2"])})

print("The total distance is:", distance_df["Distance"].sum())