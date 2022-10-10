from google import search

KEYWORDS="admin | index of '/admin' | cpanel | admin login | admin.php"

data = []
for data in search(KEYWORDS, tld='com', stop = 10):
    result.append(data)
print(data)