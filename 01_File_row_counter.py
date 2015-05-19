# -*- coding: utf-8 -*-

import sys
row_counter = 0 #行数を数える変数

argvs = sys.argv
argc=len(argvs)

if (argc != 2):   # 引数チェック
    print('Usage: # python %s filename' % argvs[0])
    quit()        # プログラムの終了

with open(argvs[1],'r', encoding='utf-8') as candidate_f:
	for row in candidate_f:
		row_counter += 1
print(row_counter)
