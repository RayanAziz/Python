# Used to make requests
import requests

# The URL to read from
URL = 'https://raw.githubusercontent.com/RayanGary/Python/master/URL%20Read/example.txt'

# Fetch the content from the URL
content = requests.get(URL)

keyword = 'Hello'

# Print the content
print(content.text)

if keyword in content.text:
   print("Keyword detected.")
