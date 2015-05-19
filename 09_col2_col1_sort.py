# -*- coding: utf-8 -*-
import sys

argvs = sys.argv
argc=len(argvs)

if (argc != 3):   # 引数チェック
	print('Usage: # python %s input_filename output_filename' % argvs[0])
	quit()        # プログラムの終了

out_list=[]

i=0

with open(argvs[1],'r', encoding='utf-8') as candidate_f, open(argvs[2],'w', encoding='utf-8') as output_f:
	for row in candidate_f:
		buf = row.split("\t")
		out_list.append(buf)
		
	out_list.sort(key = lambda line:line[0],reverse = True)
	out_list.sort(key = lambda line:line[1],reverse = True)

	
	for i in range(0,len(out_list)):
		output_f.write('\t'.join(out_list[i]))


