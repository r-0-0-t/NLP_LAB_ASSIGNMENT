import read_data_set as data_read


data = data_read.data
data = data.drop("Attribution", axis=1)
print("Modified Dataset : \n\n", data.head())

data.to_csv("../Datasets/(2) Prepared Datasets/eng_bang_data.csv", index=False)


