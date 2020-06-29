from urllib.request import urlopen

# URL to read from
url = "http://textfiles.com/adventure/aencounter.txt"

file = urlopen(url)

for line in file:
	decoded_line = line.decode("utf-8")
	print(decoded_line)
