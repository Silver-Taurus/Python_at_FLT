#! /usr/bin/env python3

''' This Package-Scrapper will scrap the name of all the packages developed from the mentioned website '''

from requests import get
from bs4 import BeautifulSoup

url = 'https://qa.debian.org/developer.php?login=guptautkarsh2102@gmail.com'
response = get(url)
soup = BeautifulSoup(response.content, 'html.parser')

names = []
for tr in soup.find_all('tr'):
    try:
        name = tr.select('a')[0]['name']
    except KeyError:
        continue
    else:
        names.append(name)
print(names)