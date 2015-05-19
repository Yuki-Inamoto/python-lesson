# -*- coding: utf-8 -*-
import sys

param = sys.argv

with open(param[1],'r', encoding='utf-8') as candidate_f, open("map.txt",'w', encoding='utf-8') as map_f:
	for row in candidate_f:
		split_row = row.split("\t")
		map_f.write(split_row[0] + "\t1" + "\n")

wordcounter = {}

with open("map.txt",'r', encoding='utf-8') as map_f:
	for row in map_f:
		word,count = row.split("\t", 1)
		count=int(count)
		wordcounter[word]=wordcounter.get(word,0) + count


	for line in wordcounter:
		print(line + " / " + str(wordcounter[line]))

	
