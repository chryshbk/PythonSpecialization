from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Author: Chrystian Santos
# Date: April 12, 2018
# Details: This file retrieves all of the anchor tags and counts the numbers from a list after being parsed by BeautifulSoup.


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
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