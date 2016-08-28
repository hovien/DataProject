# coding=utf-8

import sys

input_file = open(sys.argv[1])
adj_list = open(sys.argv[2])
noun_list = open(sys.argv[3])
output_file = sys.stdout
relation = sys.argv[4]

output_file.write("@relation {}\n".format(relation))

#creating a list of sentences from the input file
line_list = []
for line in input_file:
    line = line.rstrip()
    line_list.append(line) 

#writing the adjectives as attributes into the file
attr_list = list(adj_list)
attributes = []

for adj in attr_list:
    attributes.append(adj.strip())

for word in attributes:
    line = "@attribute " + "'{}'".format(word) + " numeric"
    output_file.write(line + "\n")

#writing the data into the file
output_file.write("@data\n")

#going through the nouns as rows in the table
noun_rows = list(noun_list)
rows = []
for noun in noun_rows:
    rows.append(noun.strip())

for row in rows:
    output_line = ""
    # each row contains the frequency of the attributes near the row attribute
    for attribute in attributes:
        counter = 0
        for line in line_list:
            line_words = line.split(" ")
            # checking if the sentence contains both the row and column attribute    
            if attribute in line_words and row in line_words:
                row_word_index = line_words.index(row)
                # applying a 4 word max distance between the two attributes
                if row_word_index > 3:
                    left = row_word_index - 4
                else:
                    left = 0
                if len(line_words) > row_word_index + 4:
                    right = row_word_index + 4
                else:
                    right = len(line_words) - 1
                # increasing the counter if the column attribute is within the 4 word window
                if attribute in line_words[left:row_word_index] or attribute in line_words[(row_word_index + 1):right]:   
                    counter += 1
        output_line = output_line + str(counter) + ","               
    
    output_line = output_line.rstrip(",")
    output_file.write(output_line + "\n")    
