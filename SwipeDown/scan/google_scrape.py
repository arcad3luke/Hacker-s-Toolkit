import requests
import bs4

query = "allinurl: index of '/admin'"

url = 'https://www.google.com/search?q=' + query
result = requests.get(url)

soup = bs4.BeautifulSoup(result.text, 'html.parser')

tags = soup.find_all()
search = soup.find("div", class_='BNeawe').text

# print(soup)

count = 0

while count <= 2:
    for x in soup.find_all(limit=1):
        if len(x.getText(strip=True)) == 0:
            x.extract()
        for tag in tags:
            print(tag.getText().split('\n'))
            print('---------')
        count += 1
        with open('scraping.txt','a+') as f:
            f.writelines(search)
            f.close()