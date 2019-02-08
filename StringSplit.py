# Author: Chrystian Santos
# Date: April 19, 2018
# Details: This program splits words in lines started with "From", gets the hours in a line and appends it in a list.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = dict()
listOfHours = list()

for line in handle:
    if not line.startswith("From"): continue
    words = line.split()
    if(len(words) < 3): continue
    time = words[5].split(":")
    hours[time[0]] = hours.get(time[0], 0) + 1

for key, value in hours.items():
    listOfHours.append((key, value))
    
listOfHours.sort()

for hour, count in listOfHours:
    print (hour, count)