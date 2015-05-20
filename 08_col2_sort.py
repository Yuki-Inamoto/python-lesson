# -*- coding: utf-8 -*-
import sys

argvs = sys.argv
argc = len(argvs)

if (argc != 3):   # 引数チェック
    print('Usage: # python %s input_filename output_filename' % argvs[0])
    raise SystemExit()  # プログラムの終了

out_list = []
i = 0

with open(argvs[1], 'r', encoding='utf-8') as candidate_f,\
        open(argvs[2], 'w', encoding='utf-8') as output_f:
    for row in candidate_f:
        buf = tuple(row.split("\t"))
        out_list.append(buf)

    sorted_out_list = sorted(out_list, key=lambda line: line[1])

    for len in sorted_out_list:
        output_f.write(len[0] + "\t" + len[1])
