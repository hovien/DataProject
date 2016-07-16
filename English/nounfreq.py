import re
import sys

#input is the file created by the POS tagger
txtinput = sys.stdin
txtoutput = sys.stdout
text = txtinput.read()

#finding all the nouns from the text
nounlist = re.findall("([a-zA-Z]*)_NN ", text)

#finding the plurals and making them singular
plural_nounlist = re.findall("([a-zA-Z]*)_NNS", text)
singular_nounlist = [noun[:-1] for noun in plural_nounlist]
nounlist.extend(singular_nounlist)

nounfreq = {}
freqlist = []

#filtering out the citations, counting the frequencies and saving them in a dictionary
for noun in nounlist:
    if len(noun) <= 1:
        continue
    if noun == "CITATION":
        continue
    noun_lower = noun.lower()    
    if not noun_lower in nounfreq:
        nounfreq[noun_lower] = 1
    else:
        nounfreq[noun_lower] += 1

#converting the dictionary into a list of lists, sorting it, writing into file
for key,value in nounfreq.items():
    freqlist.append([value, key])
freqlist.sort(reverse = True)
for item in freqlist:
    txtoutput.write(str(item) + "\n")
