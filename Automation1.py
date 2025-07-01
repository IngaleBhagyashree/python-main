from bs4 import BeautifulSoup
import requests

res = requests.get('https://example.com')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.title.text)
