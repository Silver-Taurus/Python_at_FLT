#! /usr/bin/env python3

''' Web Scraping to get the blog '''

import requests
import bs4

res = requests.get('https://www.thegoldbugs.com/bog')
soup = bs4.BeautifulSoup(res.text, 'lxml')

blog = soup.select('.sqs-block-content')

print(blog)