# coding=utf-8

import re
import sys

#input is the nounfrequency list
input_file = sys.stdin
output_file = sys.stdout

attribute_list = []

for line in input_file:
    numlist = re.findall("([0-9]+) ", line)
    num = numlist[0]
    if num > 1:
        word = re.findall("[2-9]+ ([a-zäö]+)", line)
        attribute_list.extend(word)
   
for item in attribute_list:
    output_file.write(item + "\n")
