#! /usr/bin/env python3

''' Python script to automate the task of Adding a new Github Repository '''

import requests
import getpass
import json

# Taking the details of the User
user_name = input('User Name: ')
password =  getpass.getpass()

# Taking the Repo name and description
repo_name = input('Enter the Repo name: ')
description = input('Enter the description about the repo: ')

# Formatting the repo data into json object
data = json.dumps({'name': repo_name, 'description': description})

# Posting the New Repo on the Github using Github's API
post = requests.post('https://api.github.com/user/repos', data=data, auth=(user_name, password))

# Returning the result
print(post.status_code)
