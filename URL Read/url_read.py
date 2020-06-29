# Used to make requests
import requests
# Alternative library for the same purpose
from urllib.request import urlopen

# The URL to read from
URL = 'https://raw.githubusercontent.com/RayanGary/Python/master/URL%20Read/example.txt'

# Fetch the content for use in the second library
content2 = urlopen(URL)
# Fetch the content from the URL using the first library then print it
content = requests.get(URL)

# Print the content using the first library
print(content.text)
# Decode the page in utf-8 then print it using the second library
print(content2.read().decode('utf8'))
