from urllib.request import urlopen

# URL to read from
url = "https://raw.githubusercontent.com/RayanGary/Python/master/URL%20Read/example.txt"

file = urlopen(url)

for line in file:
	decoded_line = line.decode("utf-8")
	print(decoded_line)
