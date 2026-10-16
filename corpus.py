import gzip
import json
import matplotlib.pyplot as plt
from collections import Counter
import string

PUNCT = string.punctuation + "“”‘’—–…"

path = "data/gutenberg-poetry-v001.ndjson.gz"
corpus = gzip.open(path, "rt")
numbers =[]
longlines = []
longlinebooks = []
lastwords =[]
firstwords = []
allwords = []


for row in corpus:
        d = json.loads(row)
        line = d["s"]
        book = d["gid"]
        numbers.append(len(line))

        clean_words = []
        for w in line.split():
            w = w.lower().strip(PUNCT)
            if w:
                 clean_words.append(w)
        
        if clean_words:
             firstwords.append(clean_words[0])
             lastwords.append(clean_words[-1])
             allwords.extend(clean_words)

        if len(line) >= 65:
             longlines.append(line)
             longlinebooks.append(book)

last_counts = Counter(lastwords)
first_counts = Counter(firstwords)
all_counts = Counter(allwords)
book_counts = Counter(longlinebooks)

topwords = []
topwordscounts = []
for word, count in last_counts.most_common(20):
    topwords.append(word)
    topwordscounts.append(count)

print(last_counts.most_common(20))


topfirstwords = []
topfirstwordscounts = []
for word, count in first_counts.most_common(20):
    topfirstwords.append(word)
    topfirstwordscounts.append(count)

#print(first_counts.most_common(20))


neverfirst = []
neverfirstcounts = []

for word, count in all_counts.most_common(3000):
    if word not in first_counts:
        neverfirst.append(word)
        neverfirstcounts.append(count)
#print(neverfirst, neverfirstcounts)


toplonglinebooks = []
toplonglinebookcounts = []
for word, count in book_counts.most_common(20):
    toplonglinebooks.append(word)
    toplonglinebookcounts.append(count)


plt.figure()
plt.hist(numbers, bins=30, edgecolor="black", color = "green")
plt.title("Distribution of Line Lengths")
plt.xlabel("Line length")
plt.ylabel("Number of lines")
output_dir = "plots/line_lengths.jpg"
plt.savefig(output_dir)
plt.close()
#plt.show()

output_dir2 = "plots/last_words.jpg"
plt.figure()
plt.barh(topwords, topwordscounts)
plt.title("Most Common Last Words")
plt.xlabel("Frequency")
plt.ylabel("Last Words")
plt.savefig(output_dir2)
plt.close()
#plt.show()

output_dir3 = "plots/first_words.jpg"
plt.figure()
plt.barh(topfirstwords, topfirstwordscounts)
plt.title("Most Common First Words")
plt.xlabel("Frequency")
plt.ylabel("First Words")
plt.savefig(output_dir3)
plt.close()
#plt.show()

output_dir4 = "plots/never_first_words.jpg"
plt.figure()
plt.barh(neverfirst, neverfirstcounts)
plt.title("Common Words That Never Begin a Line")
plt.xlabel("Frequency")
plt.ylabel("Words")
plt.savefig(output_dir4)
#plt.show()
plt.close()

output_dir5 = "plots/long_line_books.jpg"
plt.figure()
plt.barh(toplonglinebooks, toplonglinebookcounts)
plt.title("Books with Long Lines")
plt.xlabel("Frequency")
plt.ylabel("Book GIDs")
plt.savefig(output_dir5)
plt.show()
plt.close()




