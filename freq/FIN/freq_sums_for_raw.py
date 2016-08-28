# coding=utf-8

#opening the frequency lists
#EDIT THE INPUT FIELDS HERE (NUMBER OF INPUTS HAS TO REMAIN THE SAME)
a = open("data/Finnish/results/freq/a.freq")
b = open("data/Finnish/results/freq/a.freq")
c = open("data/Finnish/results/freq/a.freq")
ch1 = open("data/Finnish/results/freq/a.freq")
d = open("data/Finnish/results/freq/a.freq")
e = open("data/Finnish/results/freq/a.freq")
inputs = [a, b, c, ch1, d, e]

#converting them into dictionaries
a_dict = {}
b_dict = {}
c_dict = {}
ch1_dict = {}
d_dict = {}
e_dict = {}
dictionaries = [a_dict, b_dict, c_dict, ch1_dict, d_dict, e_dict]
dict_names = ["A", "B", "C", "CH1", "D", "E"]

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

#taking the 15 most frequent words
freq_sum_list = sorted(summed_freq_dict.values(), reverse = True)
most_freq_words = []
for k, v in summed_freq_dict.iteritems():
    #CHANGE "15" TO EXTEND OR RESTRICT THE LIST OF MOST FREQUENT WORDS 
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
#EDIT THE OUTPUT HERE
output_file = open("data/analysis/rawanalysis.csv", "w")

for tup in output_lines:
    word = str(tup[0])
    freq = str(tup[1])
    interv = tup[2]
    output_file.write(word + ", " + freq + ", " + interv + ", " + "\n")



        



