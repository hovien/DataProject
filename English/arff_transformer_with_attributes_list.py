# coding=utf-8

input_file = open(raw_input("Enter the input file name: "))
word_freq = open(raw_input("Enter the attribute list file name: "))
output_file = open(raw_input("Enter the output file name: "), "w")
relation = raw_input("Enter the relation name: ")

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
