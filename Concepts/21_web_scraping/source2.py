#! /usr/bin/env python3

''' Scraping Image '''

import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Cicada_3301')
soup = bs4.BeautifulSoup(res.text, 'lxml')

image_info = soup.select('.thumbimage')
print(type(image_info))
print(len(image_info))
print(image_info)
print(image_info[0])

cicada = image_info[0]

image_link = 'http:'+ cicada['src']
print(image_link)

cicada_image = requests.get(image_link, 'lxml')
with open('cicada_image.jpg', 'wb') as f:
    f.write(cicada_image.content)