# coding=utf-8

#opening the frequency lists
#EDIT THESE FILE PATHS TO CHANGE THE INPUT, THESE ARE EXAMPLES ONLY (NUMBER OF INPUTS HAS TO REMAIN THE SAME)
#SCROLL DOWN TO EDIT THE OUTPUT NAME/LOCATION
ah = open("data/English/results/freq/a.freq")
bh = open("data/English/results/freq/b.freq")
dh = open("data/English/results/freq/d.freq")
eh = open("data/English/results/freq/e.freq")
fh = open("data/English/results/freq/f.freq")
comp = open("data/English/results/freq/comp.freq")
inputs = [ah, bh, dh, eh, fh, comp]

#converting them into dictionaries
ah_dict = {}
bh_dict = {}
dh_dict = {}
eh_dict = {}
fh_dict = {}
comp = {}
dictionaries = [ah_dict, bh_dict, dh_dict, eh_dict, fh_dict, comp]

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

#making the output strings
output_lines = {}
counter = 0

for dictionary in dictionaries:
    for k, v in dictionary.iteritems():
        if k in output_lines:
            output_lines[k].append(v)
        else:
            i = 1
            output_lines[k] = list()
            while i <= counter:
                output_lines[k].append(0)
                i += 1
            output_lines[k].append(v)
    for k, v in output_lines.iteritems():
        if not k in dictionary: 
            output_lines[k].append(0)
    counter += 1

#opening output file and writing into it
#OUTPUT LOCATION/FILE NAME CAN BE EDITED HERE
output_file = open("data/analysis/analysis.csv", "w")

for k, v in output_lines.iteritems():
    output_line = k + ", "
    for num in v:
        output_line = output_line + str(num) + ", "
    output_file.write(output_line + "\n")



        



