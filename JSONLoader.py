import urllib.request as urlRequest
import json

# Author: Chrystian Santos
# Date: April 19, 2018
# Details: This file gets the location from a list and decodes it by getting its data.
address = input('Enter location: ')
if len(address) < 1: "http://py4e-data.dr-chuck.net/comments_74596.json"

print('Retrieving', address)
data = urlRequest.urlopen(address).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
address = json.loads(data);

sumCount = 0
totalCount = 0

for comment in address["comments"]:
    sumCount += int(comment["count"])
    totalCount += 1

print('Count:',totalCount)
print('Sum:',sumCount)
