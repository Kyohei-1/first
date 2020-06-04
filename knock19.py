# coding: utf-8
import pandas as pd
import sys

filePath = sys.argv[1]

df = pd.read_csv(filePath, sep='\t', header=None)
# もう定番のやつ

df_data = df[0].value_counts()
# 1コラム目のデータをascending=Falseなので降順に並び替え

print(df_data)

# python knock19.py ./popular-names.txt

# TODO:
