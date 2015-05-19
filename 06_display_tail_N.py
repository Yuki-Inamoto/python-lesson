# -*- coding: utf-8 -*-

import sys

param = sys.argv

N_row = int(param[3])
row_counter = 0
i = 0

with open(param[1],'r', encoding='utf-8') as candidate_f, open(param[2],'w', encoding='utf-8') as output_f:
	for row in candidate_f:
		row_counter += 1
	
	candidate_f.seek(0)
	
	border = row_counter - N_row

	for i in range(0,row_counter):
		buf = candidate_f.readline()
		if border <= i:
			output_f.write(buf)

