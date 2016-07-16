# coding=utf-8
import re
import sys

input_file = sys.stdin
output_file = sys.stdout

#creating a list of sentences from the input file
sentence_list = []
for line in input_file:
    stripped_line = line.strip()
    output = stripped_line.split("." or "?" or "!") 
    output = [sen.strip() for sen in output]  
    sentence_list.extend(output)

#looping through the list to write the data into the output
for sen in sentence_list:
    questions_removed = re.sub('K:.*', '', sen)
    v_removed = re.sub('V:', '', questions_removed)
    comment_removed = re.sub('\[.*\]', '', v_removed)
    words = comment_removed.split(" ")
    words = [re.sub('[^a-zäöA-ZÄÖ]', '', word) for word in words]
    words.extend(".")
    for word in words:
        output_line = ""
        uniword = word.decode("utf-8")
        output_line = uniword + "\n"
        output_file.write(output_line.encode("utf-8"))
    output_file.write("\n")        
