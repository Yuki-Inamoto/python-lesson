# -*- coding: utf-8 -*-
import sys

param = sys.argv

out_list=[]

i=0

with open(param[1],'r', encoding='utf-8') as candidate_f, open(param[2],'w', encoding='utf-8') as output_f:
	for row in candidate_f:
		buf = row.split("\t")
		out_list.append(buf)
		
	out_list.sort(key = lambda line:line[1])
	
	for i in range(0,len(out_list)):
		output_f.write('\t'.join(out_list[i]))


