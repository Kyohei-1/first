# coding: utf-8
import pandas as pd
import sys

filePath = sys.argv[1]

df = pd.read_csv(filePath, sep='\t', header=None)
# もう定番のやつ

print(df.sort_values(2, ascending=False))
# 3コラム目のデータをascending=Falseなので降順に並び替え
# 3コラム目って何や？ 行とか列とかで言ってくれ（願）

# print(df_sort)

# # TODO

# cat popular-names.txt | sort -r -n -k 3
# -r 逆順
# -n 文字列を数値とみなして並び替える
# -k 並び替える行を指定 今回は3行目
