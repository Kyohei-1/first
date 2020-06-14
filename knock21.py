# coding: utf-8
import sys
import re

path = sys.argv[1]
# ファイルのパス


def isCategory(splitedWord):
    # # カテゴリー行を正規表現で判定
    a = ''
    pattern = (
        r'^(\[\[Category:.+\]\])$'
        # 行頭から ^
        # ()中の物のグループ化
        # []はエスケープが必要だった気がするので\を付けて
        # [[Category から始まって ]] で終わる 3 桁以上の文字列なので、.+
        # $は無くても変わらないけど、付けといた。意味はよくわかってない
    )
    a = re.match(pattern, splitedWord)
    return a


with open(path, 'r') as File1:
    ReadFile = File1.readlines()
    # print(ReadFile)
    for word in ReadFile:
        splitedWord = word.split('\n')
        # 改行を消す
        splitedWord = ''.join(splitedWord)

        # print(splitedWord)
        # print(a)

        a = isCategory(splitedWord)
        if a is not None:
            # Noneのもの（カテゴリーじゃないもの）は要らないので、ここで判定
            for w in a.groups():
                # groups()で値を取ってこれるみたい。
                # groupsがないとre.Match objectとやらが返ってきた
                print(w)

        # python21.py ./knock20_result.txt
