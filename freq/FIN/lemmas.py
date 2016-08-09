# coding=utf-8
import re
import sys

#input is the file created by the POS tagger
txtinput = sys.stdin
txtoutput = sys.stdout
text = txtinput.read()

#finding all the lemmas from the text
lemmalist = re.findall("_\t([a-zäöA-ZÄÖ]*).*\[POS=.+\]", text)

lemmafreq = {}
freqlist = []

#counting the frequencies and saving them in a dictionary
for lemma in lemmalist:
    if len(lemma) <= 1:
        continue
    lemma_lower = lemma.lower().decode("utf-8")   
    if not lemma_lower in lemmafreq:
        lemmafreq[lemma_lower] = 1
    else:
        lemmafreq[lemma_lower] += 1

#converting the dictionary into a list of lists, sorting it, writing into file
for key,value in lemmafreq.items():
    freqlist.append([value, key])
freqlist.sort(reverse = True)
for lemma in freqlist:
    txtoutput.write(str(lemma[0]) + " " + lemma[1].encode("utf-8") + "\n")
