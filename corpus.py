import gzip
import json
import matplotlib.pyplot as plt
from collections import Counter

path = "data/gutenberg-poetry-v001.ndjson.gz"
corpus = gzip.open(path, "rt")
numbers =[]
longlines = []
lastwords =[]

for row in corpus:
        d = json.loads(row)
        numbers.append(len(d["s"]))
        lastwords.append(d["s"].lower().split(" ")[-1])

        if len(d["s"]) >= 65:
            longlines.append(d["s"])
        
cnt = Counter(lastwords).most_common(20)
topwords =[]
topwordscounts = []

for item in cnt:
     topwords.append(item[0])
     topwordscounts.append(item[1])
print(cnt)
print(topwords)
print(topwordscounts)

plt.hist(numbers, bins=30, edgecolor="black", color = "green")
plt.title("Distribution of Line Lengths")
plt.xlabel("Line length")
plt.ylabel("Number of lines")
output_dir = "plots/line_lengths.jpg"
plt.savefig(output_dir)
plt.show()

output_dir2 = "plots/common_words.jpg"
plt.barh(topwords, topwordscounts)
plt.savefig(output_dir2)
plt.show()




