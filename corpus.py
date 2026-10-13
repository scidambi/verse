import gzip
import json
import matplotlib.pyplot as plt
from collections import Counter
import string

path = "data/gutenberg-poetry-v001.ndjson.gz"
corpus = gzip.open(path, "rt")
numbers =[]
longlines = []
lastwords =[]
firstwords = []
allwords = []

for row in corpus:
        d = json.loads(row)
        numbers.append(len(d["s"]))
        lastwords.append(d["s"].lower().strip(string.punctuation).split(" ")[-1])
        firstwords.append(d["s"].lower().strip(string.punctuation).split(" ")[0])
        allwords.append(d["s"].lower().strip(string.punctuation).split(" "))

        if len(d["s"]) >= 65:
            longlines.append(d["s"])
        
cnt = Counter(lastwords).most_common(20)
topwords =[]
topwordscounts = []

firstcnt = Counter(firstwords).most_common(20)
topfirstwords =[]
topfirstwordscounts = []

commoncnt = Counter(allwords).most_common(20)
#topfirstwords =[]
#topfirstwordscounts = []

for item in cnt:
     topwords.append(item[0])
     topwordscounts.append(item[1])

for item in firstcnt:
     topfirstwords.append(item[0])
     topfirstwordscounts.append(item[1])

plt.hist(numbers, bins=30, edgecolor="black", color = "green")
plt.title("Distribution of Line Lengths")
plt.xlabel("Line length")
plt.ylabel("Number of lines")
output_dir = "plots/line_lengths.jpg"
plt.savefig(output_dir)
#plt.show()

output_dir2 = "plots/last_words.jpg"
plt.barh(topwords, topwordscounts)
plt.title("Most Common Last Words")
plt.xlabel("Frequency")
plt.ylabel("Last Words")
plt.savefig(output_dir2)
#plt.show()

output_dir3 = "plots/first_words.jpg"
plt.barh(topfirstwords, topfirstwordscounts)
plt.title("Most Common First Words")
plt.xlabel("Frequency")
plt.ylabel("First Words")
plt.savefig(output_dir3)
#plt.show()




