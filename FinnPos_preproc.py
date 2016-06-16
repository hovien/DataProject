# coding=utf-8
import re

input_file = open(raw_input("Enter the input file name: "))
output_file = open(raw_input("Enter the output file name: "), "w")

#creating a list of sentences from the input file
sentence_list = []
for line in input_file:
    output = line.split("." or "?" or "!")   
    sentence_list.extend(output)

#finding the longest word to be able to make coloumns in data file
len_longest = 0
for sen in sentence_list:
    words = sen.split(" ")
    for word in words:
        only_letters = re.sub('[^a-zäö]', '', word.lower())
        only_letters = only_letters.decode("utf-8")
        if len(word) > len_longest:
            len_longest = len(word)

#looping through the list to write the data into the output
for sen in sentence_list:
    output_line = ""
    words = sen.split(" ")
    for word in words:
        uniword = word.decode("utf-8")
        output_line = uniword + (len_longest - len(uniword) + 1) * " " +  "WORD=" + uniword + " LC_WORD=" + uniword.lower() + (((len_longest - len(uniword)) * 2) + 1) * " " + 3 * ("_" + 4 * " ")
    
    output_file.write(output_line + "\n")    
