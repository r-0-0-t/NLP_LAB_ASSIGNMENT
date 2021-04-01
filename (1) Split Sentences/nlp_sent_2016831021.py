import re
import pandas as pd


data = pd.read_csv("../Datasets/(2) Prepared Datasets/eng_bang_data.csv")
bangle_data = data["Bangla"]
bangle_sentences = []
count = 1


for data in bangle_data:
    sentences = re.split(r'[!?.।]+ +', data)
    if len(sentences) > 1:
        print("(", count, ")", sentences, " - ", len(sentences))
        count += 1

    for sen in sentences:
        bangle_sentences.append(sen)


print("\nDatabase Size : ", len(bangle_data))
print("Total Number of Sentences : ", len(bangle_sentences))
