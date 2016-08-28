# coding=utf-8

#opening the frequency lists
#EDIT THE INPUT HERE (NUMBER OF INPUTS HAS TO BE THE SAME)
ah = open("data/notes_AH1.txt.freq")
bh = open("data/notes_BH1.txt.freq")
dh = open("data/notes_DH1.txt.freq")
eh = open("data/notes_EH1.txt.freq")
fh = open("data/notes_FH1.txt.freq")
comp = open("data/Comp-Win1252.txt.freq")
inputs = [ah, bh, dh, eh, fh, comp]

#converting them into dictionaries
ah_dict = {}
bh_dict = {}
dh_dict = {}
eh_dict = {}
fh_dict = {}
comp_dict = {}
dictionaries = [ah_dict, bh_dict, dh_dict, eh_dict, fh_dict, comp_dict]
dict_names = ["A", "B", "D", "E", "F", "Comptel"]

counter = 0

for interview in inputs:
    for line in interview:
        word = line[2:].strip()
        number = int(line[:2])
        dictionaries[counter][word] = number
    counter += 1

#summing the frequencies
summed_freq_dict = {}

for dictionary in dictionaries:
    for k, v in dictionary.iteritems():
        if k in summed_freq_dict:
            summed_freq_dict[k] = summed_freq_dict[k] + v
        else:
            summed_freq_dict[k] = v

#taking the 50 most frequent words
freq_sum_list = sorted(summed_freq_dict.values(), reverse = True)
most_freq_words = []
for k, v in summed_freq_dict.iteritems():
    #EDIT THIS NUMBER TO CHANGE THE LENGTH OF THE FREQUENCY LIST
    if v > freq_sum_list[15]:
        most_freq_words.append(k)

#making the output lines as lists
output_lines = []
counter = 0

for dictionary in dictionaries:
    for k in most_freq_words:
        if k in dictionary:
            tup = (k, dictionary[k], dict_names[counter])
        else:
            tup = (k, 0, dict_names[counter])
        output_lines.append(tup)
    counter += 1
        

#opening output file and writing into it
#EDIT THE OUTPUT LOCATION AND FILE NAME HERE
output_file = open("data/analysis/rawTop10wordsByInt.csv", "w")

for tup in output_lines:
    word = str(tup[0])
    freq = str(tup[1])
    interv = tup[2]
    output_file.write(word + ", " + freq + ", " + interv + ", " + "\n")



        



