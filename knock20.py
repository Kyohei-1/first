# coding: utf-8

import pandas as pd
import sys

path = sys.argv[1]
# ファイルのパス

df = pd.read_json(path, lines=True)
# lines=Trueにしないとエラーになるよ

print(df.query("title == 'イギリス'")["text"].values[0])
# # SQLみたいなノリでかけるやつ？

# # print(df)

with open('./knock20_result.txt', 'w') as file:
    file.write(df.query("title == 'イギリス'")["text"].values[0])
    # ファイルに書き込む。クエリを投げれる方法を見つけたのでそれで。
    # titleの部分に国名があったので、とりあえずこれを取得していく。
    # 形式は key valueだと思うので、
    # 国名（title）が'イギリス'
    # 内容（text）というキーの中身（values[0])を取得して書き込んでく。

# python knock20.py ./jawiki-country.json
