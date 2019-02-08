import urllib.request as urlRequest
import urllib.parse as urlParse
import json

# Author: Chrystian Santos
# Date: April 19, 2018
# Details: It uses the service geojson to find the location of a university or school.

serviceurl = "http://py4e-data.dr-chuck.net/geojson?"

address = input("Enter location: ")
if len(address) < 1: "University of Toronto"

params = {"sensor": "false", "address": address}
url = serviceurl + urlParse.urlencode(params)
print("Retrieving", url)
data = urlRequest.urlopen(url).read().decode("utf-8")

print("Retrieved", len(data), "characters")
info = json.loads(data)

place_id = info["results"][0]["place_id"]
print("Place id", place_id)
