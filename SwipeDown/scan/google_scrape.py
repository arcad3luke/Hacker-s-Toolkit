import requests
from bs4 import BeautifulSoup as bs

KEYWORDS="admin | index of '/admin' | cpanel | admin login | admin.php"

# Init query array
queries = []

# Construct query
query = input("Enter search query: ")
search = query.append(queries)

# URL to use
url = f'https://www.google.com/search?&q={query}'

# Fetch the page
req = requests.get(url)

# Yeet HTTP data from the interwebs and parse
pull = bs(req.text, "html.parser")

# Print to array
print(queries)