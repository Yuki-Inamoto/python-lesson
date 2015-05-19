# -*- coding: utf-8 -*-
import sys

argvs = sys.argv
argc=len(argvs)

if (argc != 2):   # �����`�F�b�N
    print('Usage: # python %s output_filename' % argvs[0])
    quit()        # �v���O�����̏I��


with open("col1.txt", 'r', encoding='utf-8') as col1_f, open("col2.txt", 'r', encoding='utf-8') as col2_f, open(argvs[1],'w') as combine_f:
	for col1 in col1_f:
		col1 = col1.rstrip()
		col2 = col2_f.readline()
		col2 = col2.rstrip()
		buf = col1 + "\t" + col2 + "\n"
		combine_f.write(buf)

