# -*- coding: utf-8 -*-
import sys

argvs = sys.argv
argc=len(argvs)

if (argc != 3):   # 引数チェック
    print('Usage: # python %s input_filename output_filename' % argvs[0])
    quit()        # プログラムの終了

with open(argvs[1], 'r', encoding='utf-8') as candidate_f, open(argvs[2], "w") as f:
	for row in candidate_f:
		row = row.replace('\t', ' ') #タブを空白に置き換え
		f.write(row)

