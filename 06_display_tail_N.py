# -*- coding: utf-8 -*-

import sys

argvs = sys.argv
argc=len(argvs)

if (argc != 4):   # �����`�F�b�N
	print('Usage: # python %s input_filename output_filename num' % argvs[0])
	quit()        # �v���O�����̏I��
	
N_row = int(argvs[3])

row_counter = 0
i = 0

with open(argvs[1],'r', encoding='utf-8') as candidate_f, open(argvs[2],'w', encoding='utf-8') as output_f:
	for row in candidate_f: #�t�@�C�����̍s���̃J�E���g
		row_counter += 1
	
	candidate_f.seek(0)
	
	border = row_counter - N_row #�t�@�C���ɏ������ލs�̋��E���i�[

	for i in range(0,row_counter):
		buf = candidate_f.readline()
		if border <= i:
			output_f.write(buf)
