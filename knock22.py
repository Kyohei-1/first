# coding: utf-8
import sys
import re

path = sys.argv[1]
# ファイルのパス


def isCategory(splitedWord):
    # # カテゴリー行を正規表現で判定
    a = ''
    pattern = (
        r'(\[\[Category:.+\]\])'
        # 行頭から ^
        # ()中の物のグループ化
        # []はエスケープが必要だった気がするので\を付けて
        # [[Category から始まって ]] で終わる 3 桁以上の文字列なので、.+
        # $は行末にあっても取るよ
    )
    a = re.match(pattern, splitedWord)
    return a


def pickInnerWord(text):
    text = re.sub(r"\W", "", text)
    # \Wで英数字以外を置換
    text = text.replace('Category', '')
    # 邪魔なので置換
    return text


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
                # print(w)
                w = pickInnerWord(w)
                print(w)

        # 実行結果
        # [[Category:イギリス|*]]
        # [[Category:イギリス連邦加盟国]]
        # [[Category:英連邦王国 | *]]
        # [[Category:G8加盟国]]
        # [[Category:欧州連合加盟国 | 元]]
        # [[Category:海洋国家]]
        # [[Category:現存する君主国]]
        # [[Category:島国]]
        # [[Category:1801年に成立した国家・領域]]

        # python knock22.py ./knock20_result.txt
