# -*- coding: utf-8 -*-
import sys

argvs = sys.argv
argc = len(argvs)

if (argc != 4):   # 引数チェック
    print('Usage: # python %s input_filename output_filename num' % argvs[0])
    raise SystemExit()        # プログラムの終了

display = int(argvs[3])
i = 0

with open(argvs[1], 'r', encoding='utf-8') as candidate_f,\
        open(argvs[2], 'w', encoding='utf-8') as output_f:

    for i in range(0, display):
        buf = candidate_f.readline()
        output_f.write(buf)
