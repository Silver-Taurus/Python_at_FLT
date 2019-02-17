#! /usr/bin/env python3

''' Script for getting used with regular expression (re) '''
import re

# some data to use for searching
text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789

MataCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
    
coreyms.com

321-555-4321
123.555.1234
454*467*8623
802-555-4321
920-555-4321

Mr Schafer
Mr. Silver
Ms. Mavis
Mrs. Bisco
Mr. T

cat
mat
bat
pat
sat
rat

CoreyMSchafer@gmail.com
corey.schafer@university.edu
coery-321-schafer@my-work.net
'''
sentence = 'Start a sentence and then bring it to an end'


# raw string
#   --> r'...' will take \ characters as string and not as a special escape sequence.


# Searching for all the matches in a text

# make a pattern object for finding the string 'abc'
pattern = re.compile(r'abc')    
# gives an iterable providing all the matches to a string in a text
matches = pattern.finditer(text_to_search)
# iterate over all the matches
for match in matches:
    print(match)
# It is case sensitive

# In regex . is one of the meta characters and is escaped
# and in order to find that we have to use \ along with . or
# with any other meta characters mentioned above
pattern = re.compile(r'coreyms\.com')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# MetaCharacters and special escape sequences:
#   .   --> Matches any character except new line
#   \d  --> Digit(0-9)
#   \D  --> Not a Digit
#   \w  --> Word Character(a-z, A-Z, 0-9, _)
#   \W  --> Not a Word Character
#   \s  --> Whitespace(space, tab, newline)
#   \S  --> Not a Whitespace
#   \b  --> Word Boundary
#   \B  --> Not a Word Boundary
#   ^   --> Beginning of a String
#   $   --> End of a String
#   []  --> Matches Characters in brackets (Character Set)
#   [^] --> Matches Characters not in brackets
#   |   --> either ot
#   ( ) --> Group

# example: find all digits
pattern = re.compile(r'\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# example: \b
pattern = re.compile(r'\bMr')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# example: ^
# matches as Start is in the beginning of the string
pattern = re.compile(r'^Start')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)
# doesn't matches a though it is in the string but not at the start 
pattern = re.compile(r'^a')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)

# example: $
pattern = re.compile(r'end$')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)


# using metacharacters

# match phone number having any separator - or .
# (or any other pattern) between them.
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# match phone number having separator - or . only
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# for matching the number starting from 8.. or 9.. numbers
pattern = re.compile(r'[89]\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# for matching form 1 to 5 digits range
pattern = re.compile(r'[1-5]')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# for negating the matching options
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# Quantifiers:
#   *       --> 0 or more
#   +       --> 1 or more
#   ?       --> 0 or one
#   {3}     --> exact number
#   {3,5}   --> Range of numbers

# for getting phone numbers using quantifiers
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# for matching the name for differnet prefixes for Mr
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# for matching all the prefixes using a group
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# For matching the different email-id patterns from the above text
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# For matching various urls and get the data from the url
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
matches = pattern.finditer(urls)
for match in matches:
    print(match)


# In order to get the information of a specific part of the pattern
# we can make that part a group and then access it using group
# function which gives the particular group out of all the available
# groups in the matche from the matches.
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))


# Substituion using re
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)
# This helps you in re-formatting a text file
