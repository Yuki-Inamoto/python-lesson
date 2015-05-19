# -*- coding: utf-8 -*-
import sys

param = sys.argv

with open(param[1],'r', encoding='utf-8') as candidate_f, open("col1.txt",'w', encoding='utf-8') as col1_f, open("col2.txt",'w', encoding='utf-8') as col2_f:
	for row in candidate_f:
		split_row = row.split("\t")
		col1_f.write(split_row[0] + "\n")
		col2_f.write(split_row[1])


