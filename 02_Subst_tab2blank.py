# -*- coding: utf-8 -*-
import sys

param = sys.argv

with open(param[1], 'r', encoding='utf-8') as candidate_f, open(param[2], "w") as f:
	for row in candidate_f:
		row = row.replace('\t', ' ')
		f.write(row)

