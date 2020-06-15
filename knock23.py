# coding: utf-8
import sys
import re

path = sys.argv[1]
# ファイルのパス

with open(path, 'r') as File1:
    ReadFile = File1.readlines()
    # print(ReadFile)
    for word in ReadFile:
        splitedWord = word.split('\n')
        # 改行を消す
        splitedWord = ''.join(splitedWord)

        # print(splitedWord)

        # print(a)

        pattern = (
            r'(=+)\s*([^=\s]+)\s*=+'
        )
        a = ''

        a = re.match(pattern, splitedWord)
        # print(a)
        # a = ''.join(a)
        # print(a)

        if a is not None:
            Word = ''
            Count = 0
            # print(a)
            #     # Noneのもの（カテゴリーじゃないもの）は要らないので、ここで判定
            # print(a)
            for w in a.groups():
                if not '=' in w:
                    Word = w
                    # print(Word)
                    # print(Word+''+str(Count))

                if '=' in w:
                    Count = w.count('=')-1
                    # print(Count)

                print(Word+''+str(Count))

            #         # groups()で値を取ってこれるみたい。
            #         # groupsがないとre.Match objectとやらが返ってきた
            # print(w.count('='))
            # print(w+'\n')
            # pattern = re.compile(
            #     r'^(={2,})\s*(.+?)\s*\1.*$',
            #     re.MULTILINE + re.VERBOSE)
            # print(pattern.findall(w))
            # print(result)

            # print(w)

            # print(a)

            # python knock23.py ./knock20_result.txt

# 実行結果
# 1
# 国名1
# 1
# 歴史1
# 1
# 地理1
# 2
# 主要都市2
# 2
# 気候2
# 1
# 政治1
# 2
# 元首2
# 2
# 法2
# 2
# 内政2
# 2
# 地方行政区分2
# 2
# 外交・軍事2
# 1
# 経済1
# 2
# 鉱業2
# 2
# 農業2
# 2
# 貿易2
# 2
# 不動産2
# 2
# エネルギー政策2
# 2
# 通貨2
# 2
# 企業2
# 3
# 通信3
# 1
# 交通1
# 2
# 道路2
# 2
# 鉄道2
# 2
# 海運2
# 2
# 航空2
# 1
# 科学技術1
# 1
# 国民1
# 2
# 言語2
# 2
# 宗教2
# 2
# 婚姻2
# 2
# 移住2
# 2
# 教育2
# 2
# 医療2
# 1
# 文化1
# 2
# 食文化2
# 2
# 文学2
# 2
# 哲学2
# 2
# 音楽2
# 3
# ポピュラー音楽3
# 2
# 映画2
# 2
# コメディ2
# 2
# 国花2
# 2
# 世界遺産2
# 2
# 祝祭日2
# 2
# スポーツ2
# 3
# サッカー3
# 3
# クリケット3
# 3
# 競馬3
# 3
# モータースポーツ3
# 3
# 野球3
# 3
# カーリング3
# 3
# 自転車競技3
# 1
# 脚注1
# 1
# 関連項目1
# 1
# 外部リンク1
