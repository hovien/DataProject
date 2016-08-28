# coding=utf-8
import re
import sys
import Stemmer

#input is the file created by the POS tagger
txtinput = sys.stdin
txtoutput = sys.stdout
text = txtinput.read()
stemmer = Stemmer.Stemmer('finnish')

#finding all the verbs from the text
verblist = re.findall("_\t([a-zäöA-ZÄÖ]*).*\[POS=VERB\]", text)

stemmed_verblist = []
verbfreq = {}
freqlist = []

#stemming the verb list
for verb in verblist:
    stemmed_verb = stemmer.stemWords([verb])
    stemmed_verblist.extend(stemmed_verb)

#counting the frequencies and saving them in a dictionary
for verb in stemmed_verblist:
    if len(verb) <= 1:
        continue
    verb_lower = verb.lower().decode("utf-8")   
    if not verb_lower in verbfreq:
        verbfreq[verb_lower] = 1
    else:
        verbfreq[verb_lower] += 1

#converting the dictionary into a list of lists, sorting it, writing into file
for key,value in verbfreq.items():
    freqlist.append([value, key])
freqlist.sort(reverse = True)
for verb in freqlist:
    txtoutput.write(str(verb[0]) + " " + verb[1].encode("utf-8") + "\n")
