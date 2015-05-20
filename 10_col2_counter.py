# -*- coding: utf-8 -*-
import sys

argvs = sys.argv
argc = len(argvs)

if (argc != 2):   # 引数チェック
    print('Usage: # python %s col2.txt' % argvs[0])
    raise SystemExit()  # プログラムの終了

with open("col2.txt", 'r', encoding='utf-8') as candidate_f,\
        open("map.txt", 'w', encoding='utf-8') as map_f:

    for row in candidate_f:
        map_f.write(row.rstrip() + "\t" + "1" + "\n")

wordcounter = {}

with open("map.txt", 'r', encoding='utf-8') as map_f,\
        open("result.txt", 'w', encoding='utf-8') as res_f:
    for row in map_f:
        word, count = row.split("\t", 1)
        count = int(count)
        wordcounter[word] = wordcounter.get(word, 0) + count

    sorted_list = sorted(
        wordcounter.items(),
        key=lambda line: line[1],
        reverse=True
    )

    for word, count in sorted_list:
        res_f.write(word + " / " + str(count) + "\n")
