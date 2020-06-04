# coding: utf-8

import sys

filePath = ''.join(sys.argv[1])
# ファイルのパスをゲット

line = int(sys.argv[2])
# 行数の指定値をゲット

text = ''
# テキストを入れるやつを作っとく

with open(filePath, 'r', encoding='utf-8') as fileData:
    # 読み込みでファイルを開く

    for i in range(line):
      # lineの数だけ繰り返す

        text += fileData.readline()
        # 内容を読み込んでテキストに追加する

print(text.strip())
# 表示

# python knock14.py /Users/kyohei/Desktop/100knock/popular-names.txt 3
