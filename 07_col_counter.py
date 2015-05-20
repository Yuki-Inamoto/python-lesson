# -*- coding: utf-8 -*-
import sys

argvs = sys.argv
argc = len(argvs)

if (argc != 2):   # 引数チェック
    print('Usage: # python %s input_filename' % argvs[0])
    raise SystemExit()  # プログラムの終了

with open(argvs[1], 'r', encoding='utf-8') as candidate_f:
    for row in candidate_f:
        split_row = row.split("\t")  # 1行をtabで分割
        # 結果出力: 出力形式: 対象文字列 / 文字数
        print(split_row[0] + " / " + str(len(split_row[0])))
