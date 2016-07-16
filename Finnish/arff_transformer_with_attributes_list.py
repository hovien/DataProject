# coding=utf-8

import sys

input_file = open(sys.argv[1])
word_freq = open(sys.argv[2])
output_file = sys.stdout
relation = sys.argv[3]

output_file.write("@relation {}\n".format(relation))

#creating a list of sentences from the input file
line_list = []
for line in input_file:
    line = line.rstrip()
    line_list.append(line) 

#writing the attributes into the file
word_list = list(word_freq)
attributes = []

for word in word_list:
    attributes.append(word.strip())

for word in attributes:
    line = "@attribute " + "'{}'".format(word) + " { t}"
    output_file.write(line + "\n")

#writing the data into the file
output_file.write("@data\n")

for line in line_list:
    output_line = ""
    for word in attributes:
        if word not in line:
            output_line += "?,"
        else:
            output_line += "t,"
    
    output_line = output_line.rstrip(",")
    output_file.write(output_line + "\n")    
