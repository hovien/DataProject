# coding=utf-8

import re

#input is the nounfrequency list
input_file = open(raw_input("enter input file: "))
output_file = open(raw_input("enter output file: "), "w")

attribute_list = []

for line in input_file:
    item = line.rstrip("]").lstrip("[")
    if int(item[0]) > 1:
        word = re.find("[2-9]+, '([a-z])'", item)
        attribute_list.append(word)
   

for item in attribute_list:
    output_file.write(item + "\n")
