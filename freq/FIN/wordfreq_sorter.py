# coding=utf-8

import chardet
import sys

freqs = sys.stdin
sorted_freqs = sys.stdout

sorted_freqs_list = []

for line in freqs:
    line = line.strip()
    tup = (int(line[:2]), line[2:])
    sorted_freqs_list.append(tup)

sorted_freqs_list.pop(0)
sorted_freqs_list.sort(reverse = True)

for elem in sorted_freqs_list:
    string = str(elem[0]) + " " + elem[1].strip()
    sorted_freqs.write(string + "\n")
