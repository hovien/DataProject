# coding=utf-8

import Stemmer
import re
import sys
import codecs

sentence_input = sys.stdin
stemmed_output = sys.stdout
stemmer = Stemmer.Stemmer('english')
sentence_list = []
stemmed_sentence_list = []

for line in sentence_input:
    decoded = line.decode("windows-1252")
    sentence_list.append(decoded.rstrip())
   
for sentence in sentence_list:
    stemmed_sentence = []
    one_sentence = sentence.split(" ")
    for word in one_sentence:    
        stemmed_sentence += stemmer.stemWords([word])    
    stemmed_sentence_list.append(stemmed_sentence) 

stemmed_sentence_string = ""

for sentence in stemmed_sentence_list:    
    sentence_string = ""
    for word in sentence: 
        sentence_string += word + " "    
    stemmed_sentence_string += sentence_string + "\n"   
stemmed_output.write(stemmed_sentence_string.encode("utf-8"))
          
    


