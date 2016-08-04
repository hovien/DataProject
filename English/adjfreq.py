import re
import sys

#input is the file created by the POS tagger
txtinput = sys.stdin
txtoutput = sys.stdout
text = txtinput.read()

#finding all the nouns from the text
adj_list = re.findall("([a-zA-Z]*)_JJ", text)

adj_freq = {}
freqlist = []

#filtering out the citations, counting the frequencies and saving them in a dictionary
for adj in adj_list:
    if len(adj) <= 1:
        continue
    adj_lower = adj.lower()    
    if not adj_lower in adj_freq:
        adj_freq[adj_lower] = 1
    else:
        adj_freq[adj_lower] += 1

#converting the dictionary into a list of lists, sorting it, writing into file
for key,value in adj_freq.items():
    freqlist.append([value, key])
freqlist.sort(reverse = True)
for item in freqlist:
    txtoutput.write(str(item) + "\n")
