# -*- coding: utf-8 -*-
import sys

argvs = sys.argv
argc=len(argvs)

if (argc != 2):   # 引数チェック
	print('Usage: # python %s input_filename' % argvs[0])
	quit()        # プログラムの終了

with open(argvs[1],'r', encoding='utf-8') as candidate_f, open("map.txt",'w', encoding='utf-8') as map_f:
	for row in candidate_f:
		split_row = row.split("\t")
		map_f.write(split_row[0] + "\t1" + "\n") #map.txtに(word	1)の形式で書き込み

wordcounter = {}

with open("map.txt",'r', encoding='utf-8') as map_f:
	for row in map_f:
		word,count = row.split("\t", 1)
		count=int(count)
		wordcounter[word]=wordcounter.get(word,0) + count


	for line in wordcounter:
		print(line + " / " + str(wordcounter[line]))

	
