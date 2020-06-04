# coding: utf-8
import pandas as pd
import sys

filePath = sys.argv[1]

df = pd.read_csv(filePath, sep='\t', header=None)
# もう定番のやつ

df_sort = df.sort_values(2, ascending=False)
# 3コラム目のデータをascending=Falseなので降順に並び替え
# 3コラム目って何や？ 行とか列とかで言ってくれ（願）

print(df_sort)

# TODO:
