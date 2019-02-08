from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Author: Chrystian Santos
# Date: April 19, 2018
# Details: The user enters a link which will be opened and parsed. Then it will find all the anchor tags.
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
numbers = list()
for tag in tags:
    # Look at the parts of a tag
    numbers.append(tag.contents[0])
total = 0
for number in numbers:
	total += int(number)
print(total)