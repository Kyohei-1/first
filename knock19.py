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

# TODO
# cat popular-names.txt | cut -f 1 | sort -r -n | uniq -c -i | sort -r -n

# cut -f 1 1行目を取る
# sort -r -n 逆順にする 数字を並び替える
# uniq -c 重複は要らんから死を
# sort -r -n もう一回ちゃんと並べ直す。
