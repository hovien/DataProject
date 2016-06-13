# coding=utf-8

import chardet
freqs = open("stemmed-wordfreq.txt")
sorted_freqs = open("wordfreq_sorted.txt", "w")

sorted_freqs_list = []

for line in freqs:
    line = line.rstrip()    
    freq, word = line[6], line[8:]
    freqword = str(freq) + " " + str(word)
    sorted_freqs_list.append(freqword)

sorted_freqs_list.sort(reverse = True)

for elem in sorted_freqs_list:
    sorted_freqs.write(elem + "\n")
