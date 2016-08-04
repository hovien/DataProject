# coding=utf-8

import re
import Stemmer
import sys

#input is the nounfrequency list
input_file = sys.stdin
output_file = sys.stdout
stemmer = Stemmer.Stemmer('english')

attribute_list = []

for line in input_file:
    word = re.findall("[2-9]+, '([a-z]+)'", line)
    attribute_list.extend(word)
   
for item in attribute_list:
    output_file.write(item + "\n")
