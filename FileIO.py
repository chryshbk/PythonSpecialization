fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

# Author: Chrystian Santos
# Date: February 2, 2018
# Details: Reads the file mbox-short.txt and extracts information from it. Counts how many lines start with "from"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith("From"):
        line = line.split()
        if (len(line) > 2): print(line[1])
        if (len(line) > 2): count += 1

print("There were", count, "lines in the file with From as the first word")
