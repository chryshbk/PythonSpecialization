import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Author: Chrystian Santos
# Date: April 19, 2018
# Details: This file gets the URL and parses it. It retrieves a list of URLs in a link that was provide.

def getURL(url):
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	return soup

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1

listOfURL = list()

for _ in range(count):
	listOfTags = list()
	
	for tag in getURL(url)("a"):
		listOfTags.append(tag)
		
	url = listOfTags[position].get('href', None)
	
	print("Retrieving:",url)
	listOfURL.append(url)

print("Last URL:", listOfURL[-1])