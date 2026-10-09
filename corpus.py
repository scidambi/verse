import gzip
import json
import matplotlib.pyplot as plt


path = "data/gutenberg-poetry-v001.ndjson.gz"
corpus = gzip.open(path, "rt")


numbers =[]
longlines = []

for row in corpus:
        d = json.loads(row)
        numbers.append(len(d["s"]))

        if len(d["s"]) >= 65:
            longlines.append(d["s"])

print(longlines)

        

plt.hist(numbers, bins=30, edgecolor="black", color = "green")
plt.title("Distribution of Line Lengths")
plt.xlabel("Line length")
plt.ylabel("Number of lines")
output_dir = "plots/line_lengths.jpg"
plt.savefig(output_dir)
plt.show()




