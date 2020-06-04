# coding: utf-8
# import sys

# path = ''.join(sys.argv[1])
# # ファイルのパス取るやで

# with open(path) as fileData:
#     # ファイルを開く

#     for i in fileData:
#         # 1行ずつ読み込む
#         path = write(i)

import sys
path = sys.argv[1]

with open(path, "r") as f:
    # 一行ずつ読み込む
    for data in f:
        # TAB を 空白へ置換（strip で white space を除去）
        print(data.strip().replace("\t", " "))

# cat  ./popular-names.txt | sed s/$'\t'/' '/g
# python /Users/kyohei/Desktop/100knock/knock11.py /Users/kyohei/Desktop/100knock/popular-names.txt
