# coding=utf-8

import re
import Stemmer
import sys

#input is the nounfrequency list
input_file = sys.stdin
output_file = sys.stdout
stemmer = Stemmer.Stemmer('english')

attribute_list = []
stemmed_attr_list = []

for line in input_file:
    numlist = re.findall("([0-9]+), '", line)
    num = numlist[0]
    if num > 1:
        word = re.findall("[2-9]+, '([a-z]+)'", line)
        attribute_list.extend(word)
   
for item in attribute_list:
    stemmed_word = stemmer.stemWords([item])
    if not stemmed_word in stemmed_attr_list:
        stemmed_attr_list.append(stemmed_word)

for item in stemmed_attr_list:
    output_file.write(item[0] + "\n")
