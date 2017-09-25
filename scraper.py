import requests
from bs4 import BeautifulSoup

response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(response.content, 'html.parser')


print(list(soup.children))