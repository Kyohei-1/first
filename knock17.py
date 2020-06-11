# coding: utf-8
import pandas as pd
import sys

option1 = sys.argv[1]
# filePath

df = pd.read_csv(option1, sep='\t', header=None)
# pandasのread_csvでファイルを読み込んで、区切りは'\t'
# headerはNoneとする

df = df[0].unique()
df.sort()
print(df)
# df[0] つまり1行目の重複しないデータを取ってくる

# python knock17.py ./popular-names.txt

# TODO:
# cat popular-names.txt | cut -f 1 | sort | uniq -c
