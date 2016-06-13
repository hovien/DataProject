# coding=utf-8

import re

txtinput = open(raw_input("input file name: "),)
stop_input = open(raw_input("stop word list: "))
txtoutput = open(raw_input("output file name: "), "w")

# reading the file, splitting it into sentences, saving into a list
sentence_list = []
for line in txtinput:
    output = line.rstrip().lower()
    output = output.split("." or "?" or "!")   
    sentence_list.extend(output)

#creating the stopword list
stop_list = (stop_input.read()).split("\n")

#removing stop words and non-alphabeting characters
output_string = ""
for sentence in sentence_list:
    if len(sentence) <= 2:
        continue    
    output_sentence = ""
    one_sentence = sentence.split(" ")
    for word in one_sentence:
        if word in stop_list:
            continue
        only_letters = re.sub('[^a-zäö]', '', word)
        output_sentence += only_letters + " "
    output_string += output_sentence + "\n"

#decoding-encoding and writing the result in the output
txtoutput.write(output_string)
