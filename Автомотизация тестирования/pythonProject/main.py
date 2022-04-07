# importing the modules
from bs4 import BeautifulSoup
import requests

# URL to the scraped
URL = 'https://srr.ru/struktura/sapisok-chlenov-srr-2-2/'

# getting the contents of the website and parsing them
webpage = requests.get(URL)
soup = BeautifulSoup(webpage.content, "lxml")
# title = soup.find("tr", attrs={'id': 'members2020'})
print(soup.find('tbody').find_all('tr'))
