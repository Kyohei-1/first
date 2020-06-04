# coding: utf-8

import sys

# 面倒なので関数化


def readLinesName(file_name):
    # 読み取りモードで開く、
    with open(file_name, 'r') as file:
        # readlinesと言う関数で内容を読み込んで返す
        return file.readlines()


filePath = sys.argv[1]
# ファイルのパスをゲット

line = int(sys.argv[2])
# 行数の指定値をゲット

text = ''
# テキストを入れるやつを作っとく

lines = readLinesName(filePath)
# ファイルのパスを渡して中身を取得してきてもらう

if line != 0:
    print(''.join(lines[-1 * int(line):]).strip())
# -1を指定することで逆順に出来る
# -1だけだと最後しか取得できないので、入力された引数分をかける事で、
# 5つ取得だと、最後から-1,-2,-3,-4,-5の5つを取得できる

# python knock15.py /Users/kyohei/Desktop/100knock/popular-names.txt 5
