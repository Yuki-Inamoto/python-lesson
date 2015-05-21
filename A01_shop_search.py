#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib.request
import urllib.parse
import urllib.error
import json

####
# 変数の型が文字列かどうかチェック
####


def is_str(data=None):
    if isinstance(data, str) or isinstance(data, str):
        return True
    else:
        return False


####
# 初期値設定
####

# APIアクセスキー
keyid = ""  # accsesskey

# エンドポイントURL
url = "http://api.gnavi.co.jp/ver1/RestSearchAPI/"

# 店名を引数から取得
argvs = sys.argv
argc = len(argvs)

if (argc != 2):   # 引数チェック
    print('Usage: # python %s freeword' % argvs[0])
    quit()        # プログラムの終了

freeword = argvs[1].encode('utf-8')

####
# APIアクセス
####
# URLに続けて入れるパラメータを組立
query = [
  ("format", "json"),
  ("keyid", keyid),
  ("hit_per_page", 10),
  ("freeword", freeword)
]

# URL生成
url += "?{0}".format(urllib.parse.urlencode(query))
print(url)
# API実行
try:
    result = urllib.request.urlopen(url).read()
except ValueError:
    print("APIアクセスに失敗しました。")
    sys.exit()

####
# 取得した結果を解析
####
result = result.decode('utf-8')
data = json.loads(result)

# エラーの場合
if "error" in data:
    if "message" in data:
        print(("{0}".format(data["error"]["message"])))
    else:
        print("データ取得に失敗しました。")
    sys.exit()

# ヒット件数取得
total_hit_count = None
if "total_hit_count" in data:
    total_hit_count = data["total_hit_count"]

# ヒット件数が0以下、または、ヒット件数がなかったら終了
if total_hit_count is None or int(total_hit_count) <= 0:
    print("指定した内容ではヒットしませんでした。")
    sys.exit()

# レストランデータがなかったら終了
if "rest" not in data:
    print("レストランデータが見つからなかったため終了します。")
    sys.exit()


# レストランデータ取得
for rest in data["rest"]:
    line = []
    name = ""

    # 店舗名
    if "name" in rest and is_str(rest["name"]):
        name = "{0}".format(rest["name"])
    line.append(name)
    print("\t".join(line))

# 終了
sys.exit()
