# -*- coding: utf-8 -*-
import sys

param = sys.argv

display = int(param[3])
i=0

with open(param[1],'r', encoding='utf-8') as candidate_f, open(param[2],'w', encoding='utf-8') as output_f:
	for i in range(0,display):
		buf=candidate_f.readline()
		output_f.write(buf)

