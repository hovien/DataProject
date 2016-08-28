# coding=utf-8

import re
import sys
import codecs

txtinput = sys.stdin
stop_input = open("../DataProject/English/english_stop.txt")
abbr_input = open("../DataProject/English/abbreviations.txt")
txtoutput = sys.stdout

#creating the stopword and abbreviation list
stop_list = (stop_input.read()).split("\n")
abbr_list = (abbr_input.read()).lower().split("\n")

# reading the file, geting rid of abbreviations, splitting it into sentences, saving into a list
sentence_list = []
for line in txtinput:
    abbr_check = line.rstrip().lower().split(" ")
    output = ""
    for word in abbr_check:
        if word in abbr_list:
            del word
            continue
        output += word + " "
    output = output.split("." or "?" or "!")   
    sentence_list.extend(output)

#removing stop words, citation marks, questions and non-alphabeting characters
output_string = ""
for sentence in sentence_list:
    if len(sentence) <= 2:
        continue    
    output_sentence = ""
    citations_removed = re.sub('\[ citation .* \]', '', sentence)
    questions_removed = re.sub('q:.*\?', '', citations_removed)
    a_removed = re.sub('a:', '', questions_removed)
    one_sentence = a_removed.split(" ")
    for word in one_sentence:
        if word in stop_list:
            continue
        only_letters = re.sub('[^a-zäö]', '', word)
        output_sentence += only_letters + " "
    output_string += output_sentence + "\n"

#writing the result in the output
txtoutput.write(output_string)
