import urllib.request
import xml.etree.ElementTree as ET

# Author: Chrystian Santos
# Date: April 12, 2018
# Details: This file gets a URL and crawls into it by retrieving the data from the XML file.

url = input('Enter location: ')
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_74595.xml"

print('Retrieving', url)
	
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

numbers = tree.findall('.//count')
print ("Count:", len(numbers))

counter = 0

for number in numbers:
	counter += int(number.text)

print('Sum:', counter)