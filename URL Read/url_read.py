# I wrote this script to prove that mecai.org is just a shell organization that charges $100 to issue fake certificates that can be easily mass extracted from their website and traced back to one real company in Saudi Arabia.
import requests

# Base URL
URL = "https://www.mecai.org/cr/"

# Counter for certificate groups found
count = 0

print(URL)

# Try numbers 0 to 1000 in the URL
for cr in range (0, 1000):
	link = URL
	link += str(cr)
	link += ".php"
	content = requests.get(link)
	keyword = 'Download'

	if keyword in content.text:
		print("Certificate group found: ", link)
		count = count + 1
print ("Number of certificate groups found: ", count)
