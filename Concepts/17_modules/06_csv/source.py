#! /usr/bin/env python3

''' Python script to read a csv file '''

import csv
data = open('example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines)