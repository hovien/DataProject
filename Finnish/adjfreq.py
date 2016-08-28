# coding=utf-8
import re
import sys
import Stemmer

#input is the file created by the POS tagger
txtinput = sys.stdin
txtoutput = sys.stdout
text = txtinput.read()
stemmer = Stemmer.Stemmer('finnish')

#finding all the adjs from the text
adjlist = re.findall("_\t([a-zäöA-ZÄÖ]*).*\[POS=ADJECTIVE\]", text)

stemmed_adjlist = []
adjfreq = {}
freqlist = []

#stemming the adjective list
for adj in adjlist:
    stemmed_adj = stemmer.stemWords([adj])
    stemmed_adjlist.extend(stemmed_adj)

#counting the frequencies and saving them in a dictionary
for adj in stemmed_adjlist:
    if len(adj) <= 1:
        continue
    adj_lower = adj.lower().decode("utf-8")   
    if not adj_lower in adjfreq:
        adjfreq[adj_lower] = 1
    else:
        adjfreq[adj_lower] += 1

#converting the dictionary into a list of lists, sorting it, writing into file
for key,value in adjfreq.items():
    freqlist.append([value, key])
freqlist.sort(reverse = True)
for adj in freqlist:
    txtoutput.write(str(adj[0]) + " " + adj[1].encode("utf-8") + "\n")
