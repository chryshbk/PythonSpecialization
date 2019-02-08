import re

# Author: Chrystian Santos
# Date: April 19, 2018
# Details: Opens a txt file and finds all the numbers in a line and sums them.

handle = open("D:\\regex_sum_74591.txt")
list = list()
total = 0
for line in handle:
	list += re.findall('[0-9]+', line)
for number in list:
	total += int(number)
print(total)