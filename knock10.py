# coding: utf-8
import sys

count = 0
# カウンタ用の変数を用意

path = ''.join(sys.argv[1])
# 使うファイルのパスを指定

with open(path) as fileData:
    # withを使うとファイルを閉じるのは勝手にやってくれる...らしい。
    # asをつけたのはfileNameのインスタンス（中身）の文章を取得したいから。

    for i in fileData:
        # 1行ずつ回してカウントする

        count += 1
        # カウントを足す

    print(count)
    # ループを抜けたら表示

# python /Users/kyohei/Desktop/100knock/knock10.py /Users/kyohei/Desktop/100knock/popular-names.txt
