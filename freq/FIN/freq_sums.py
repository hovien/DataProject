# coding=utf-8
import re

#opening the frequency lists
#EDIT THESE FILE PATHS TO CHANGE THE INPUT, THESE ARE EXAMPLES ONLY (NUMBER OF INPUTS HAS TO REMAIN THE SAME)
#SCROLL DOWN TO EDIT THE OUTPUT NAME/LOCATION
a = open("data/Finnish/results/freq/a.freq")
b = open("data/Finnish/results/freq/b.freq")
c = open("data/Finnish/results/freq/c.freq")
ch1 = open("data/Finnish/results/freq/ch1.freq")
d = open("data/Finnish/results/freq/d.freq")
e = open("data/Finnish/results/freq/e.freq")
nsn0407 = open("data/Finnish/results/freq/nsn04.freq")
nsn0303 = open("data/Finnish/results/freq/nsn03.freq")
inputs = [a, b, c, ch1, d, e, nsn0407, nsn0303]

#converting them into dictionaries
a_dict = {}
b_dict = {}
c_dict = {}
ch1_dict = {}
d_dict = {}
e_dict = {}
nsn0407_dict = {}
nsn0303_dict = {}
dictionaries = [a_dict, b_dict, c_dict, ch1_dict, d_dict, e_dict, nsn0407_dict, nsn0303_dict]

counter = 0

for interview in inputs:
    for line in interview:
        word = re.findall("[a-zäö]+", line)
        word = word[0]
        number = re.findall("[0-9]+", line)
        number = number[0]
        dictionaries[counter][word] = number
    counter += 1

#storing the frequency informations in a dictionary, where the words are keys and the frequencies are values. The frequencies are saved as lists, the index showing which interview they represent
output_lines = {}
counter = 0

#looping through the interview dictionaries and adding the words to the output_lines dictionary
for dictionary in dictionaries:
    for k, v in dictionary.iteritems():
        if k in output_lines:
            output_lines[k].append(v)
        #if the word hasn't been in the first few interviews, the 0 frequencies are added to those columns
        else:
            i = 1
            output_lines[k] = list()
            while i <= counter:
                output_lines[k].append(0)
                i += 1
            output_lines[k].append(v)
   
    #if the word has been in previous interviews, but not in the current one, a 0 is added as frequency
    for k, v in output_lines.iteritems():
        if not k in dictionary: 
            output_lines[k].append(0)
    counter += 1

#opening output file and writing into it with format "word, frequency in interview A, frequency in interview B, etc."
#OUTPUT LOCATION/FILE NAME CAN BE EDITED HERE
output_file = open("data/analysis/nounanalysis.csv", "w")

for k, v in output_lines.iteritems():
    output_line = k + ", "
    for num in v:
        output_line = output_line + str(num) + ", "
    output_file.write(output_line + "\n")



        



