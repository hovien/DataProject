# coding=utf-8

from types import *

input_file = open("barack.freq.txt")
output_file = open("barack.freq.sorted.cut.txt", "w")

freq_list = []

for line in input_file:
    wordfreq = line.strip().split(" ")
    wordfreq[0] = int(wordfreq[0])
    freq_list.append(tuple(wordfreq))

freq_list.sort(reverse= True)

for i in range(200):
    
    output_file.write(freq_list[i][1] + "\n")
