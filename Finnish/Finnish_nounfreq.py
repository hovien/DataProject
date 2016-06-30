# coding=utf-8
import re

#input is the file created by the POS tagger
txtinput = open(raw_input("input file name: "),)
txtoutput = open(raw_input("output file name: "), "w")
text = txtinput.read()

#finding all the nouns from the text
nounlist = re.findall("_\t([a-zäöA-ZÄÖ]*).*\[POS=NOUN\]", text)

nounfreq = {}
freqlist = []

#counting the frequencies and saving them in a dictionary
for noun in nounlist:
    if len(noun) <= 1:
        continue
    noun_lower = noun.lower().decode("utf-8")   
    if not noun_lower in nounfreq:
        nounfreq[noun_lower] = 1
    else:
        nounfreq[noun_lower] += 1

#converting the dictionary into a list of lists, sorting it, writing into file
for key,value in nounfreq.items():
    freqlist.append([value, key])
freqlist.sort(reverse = True)
for noun in freqlist:
    txtoutput.write(str(noun[0]) + " " + noun[1].encode("utf-8") + "\n")
