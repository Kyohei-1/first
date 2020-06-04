# coding: utf-8
import sys


def readLines(fileName):
    with open(fileName, 'r') as fileData:
        return fileData.readlines()


option1 = int(sys.argv[1])
# 行数

option2 = sys.argv[2]
# ファイルのパス

fileOBJ = readLines(option2)
# 全部を読み込んで返させる

output = ''
i = int(1)
for line in range(option1):
    # option1の数だけ追加してファイルに出力
    output += fileOBJ[line]
    if i <= option1:
        i += 1
        with open('./output.txt', 'w') as file:
            file.write(output)

print(output)

# 出来とらん

# TODO:
