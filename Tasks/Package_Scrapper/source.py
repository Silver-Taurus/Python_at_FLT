#! /usr/bin/env python3

'''
This Package-Scraper will scrap the name of all the
packages developed from the mentioned website.
'''

from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
import re

def get_file_name(url):
    ''' Function to return the file name '''
    pattern = re.compile(r'https://qa\.debian\.org/developer\.php\?login=(\w+)@[a-zA-Z]+\.[a-z]+')
    matches = pattern.finditer(url)
    return [match.group(1) for match in matches][0]

def scrap(url):
    ''' Generator Function to give the scraped name of package from the required website '''
    response = get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for tr in soup.find_all('tr'):
        try:
            name = tr.select('a')[0]['name']
        except KeyError:
            continue
        else:
            yield name

def package_file(file_name, url, yld=False):
    ''' Function to access and update the package-name file '''
    with open(file_name + '.txt', 'w') as pf:
        for name in scrap(url):
            pf.write(name + '\n')
            if yld == True:
                yield name

def log_file(file_name, added_names, deleted_names=set()):
    ''' Function to access and update the log file '''

    with open(file_name + '_log.txt', 'a') as lf:
        lf.write('\n\n\nDate: {}'.format(datetime.today()))
        
        lf.write('\n\nAdded-Packages: \n')
        for name in added_names:
            lf.write(name + '\n')

        lf.write('\nDeleted-Packages: \n')
        for name in deleted_names:
            lf.write(name + '\n')

def main():
    ''' Main Driver Program '''
    url = 'https://qa.debian.org/developer.php?login=guptautkarsh2102@gmail.com'
    file_name = get_file_name(url)
    try:
        packages = {line.strip() for line in open(file_name + '.txt', 'r')}
        package_file(file_name, url)
        new_packages = {line.strip() for line in open(file_name + '.txt', 'r')}
        log_file(file_name, new_packages.difference(packages), packages.difference(new_packages))
    except FileNotFoundError:
        added_names = {name for name in package_file(file_name, url, yld=True)}
        log_file(file_name, added_names)

if __name__ == '__main__':
        main()