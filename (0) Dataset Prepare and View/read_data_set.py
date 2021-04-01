import pandas as pd


data = pd.read_csv("../Datasets/(1) Main Datasets/ben.txt", sep="\t", header=None, names=["English", "Bangla", "Attribution"])
print("Main Dataset : \n\n", data.head())
