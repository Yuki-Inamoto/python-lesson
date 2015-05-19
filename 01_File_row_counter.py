# -*- coding: utf-8 -*-
import sys
row_counter = 0

param = sys.argv

with open(param[1],'r', encoding='utf-8') as candidate_f:
	for row in candidate_f:
		row_counter += 1
print(row_counter)
