# Author: Chrystian Santos
# Date: April 19, 2018
# Details: Reads a file, gets lines that start with "From" and counts the number of words in it.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if line.startswith("From"):
        words = line.split()
        email = words[1]
        if(len(words) > 2):
        	counts[email] = counts.get(email,0) + 1
    else:
        continue
        
bigCount = None
bigWord = None

for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count
print(bigWord, bigCount)