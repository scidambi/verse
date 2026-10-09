import gzip
import json
import matplotlib.pyplot as plt



path = "data/gutenberg-poetry-v001.ndjson.gz"
corpus = gzip.open(path, "rt")


numbers =[]

for row in corpus:
        d = json.loads(row)
        numbers.append(len(d["s"]))
        

plt.hist(numbers, bins=30, edgecolor="black", color = "green")
plt.show()



