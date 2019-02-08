# Author: Chrystian Santos
# Date: February 02, 2018
# Details: Reads a file from the computer and split the words in a line, storing them in a list and sorting them.

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for word in line.split():
        if word not in lst:
    		lst.append(word)            
lst.sort()
print(lst)