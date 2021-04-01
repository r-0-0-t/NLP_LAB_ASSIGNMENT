import pandas as pd


data = pd.read_csv("../Datasets/(2) Prepared Datasets/eng_bang_data.csv")

print("(1) Prepared Dataset : \n\n", data.head())
print("\n\n(2) Number of Data : \n\n".format(data.count().sum()), data.count())
print("\n\n(3) Null Data Items :\n\n", data.isna().sum())
print("\n\n(4) Description of Dataset : \n\n", data.describe())