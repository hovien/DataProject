import re
import sys
import Stemmer

#input is the file created by the POS tagger
txtinput = sys.stdin
txtoutput = sys.stdout
text = txtinput.read()
stemmer = Stemmer.Stemmer('english')

stop_input = open("../DataProject/English/english_stop.txt")
stop_list = (stop_input.read()).split("\n")

#finding all the verbs from the text
verb_list = re.findall("([a-zA-Z]*)_VB.*?", text)

stemmed_verb_list = []
verbfreq = {}
freqlist = []

#stemming the verbs
for verb in verb_list:
    stemmed_word = stemmer.stemWords([verb])
    stemmed_word = stemmed_word[0].lower()
    stemmed_verb_list.append(stemmed_word)

#filtering out stop words, counting the frequencies and saving them in a dictionary
for verb in stemmed_verb_list:
    if len(verb) <= 1:
        continue
    if verb in stop_list:
        continue    
    if not verb in verbfreq:
        verbfreq[verb] = 1
    else:
        verbfreq[verb] += 1

#converting the dictionary into a list of lists, sorting it, writing into file
for key,value in verbfreq.items():
    freqlist.append([value, key])
freqlist.sort(reverse = True)
for item in freqlist:
    txtoutput.write(str(item) + "\n")
