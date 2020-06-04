# coding: utf-8

import pandas as pd
# pandasの中身は知らんけど、便利らしい pdって名前で呼び出す
import sys
path = sys.argv[1]
# いつも通りのやつ 引数を取得して入れとく
path = path.strip()
# デフォルトでは両端の連続する空白文字が取り除かれる。改行\nや全角スペース\u3000やタブ\tも空白文字とみなされ削除される。らしい。

df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
# 区切り文字をdelimiterで設定。
# headerは知らんけど無いと思うからNone
df.iloc[:, 0].to_csv('col1.txt', sep=' ', header=False, index=False)
# 1行目の列（名前のところを取得？）
df.iloc[:, 1].to_csv('col2.txt', sep=' ', header=False, index=False)
# 2行目の列（名前のところを取得？）

# python /Users/kyohei/Desktop/100knock/knock12.py /Users/kyohei/Desktop/100knock/popular-names.t
