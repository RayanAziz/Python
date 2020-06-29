#Used to make requests
from urllib.request import urlopen

# The URL to read from
URL = urlopen('https://raw.githubusercontent.com/RayanGary/Python/master/URL%20Read/example.txt')

# Decode the page in utf-8 and print it
print(URL.read().decode('utf8'))
