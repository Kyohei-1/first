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
            # print(a)
            #     # Noneのもの（カテゴリーじゃないもの）は要らないので、ここで判定
            # print(a)
            Word = None
            Count = None
            for w in a.groups():
                if not '=' in w:
                    Word = w
                    # print(Word)
                    # print(Word+''+str(Count))
                elif '=' in w:
                    Count = w.count('=')-1
                    # print(Count)
                if Word is None:
                    print('')
                elif Count is None:
                    print('')
                else:
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
# 国名1

# 歴史1

# 地理1

# 主要都市2

# 気候2

# 政治1

# 元首2

# 法2

# 内政2

# 地方行政区分2

# 外交・軍事2

# 経済1

# 鉱業2

# 農業2

# 貿易2

# 不動産2

# エネルギー政策2

# 通貨2

# 企業2

# 通信3

# 交通1

# 道路2

# 鉄道2

# 海運2

# 航空2

# 科学技術1

# 国民1

# 言語2

# 宗教2

# 婚姻2

# 移住2

# 教育2

# 医療2

# 文化1

# 食文化2

# 文学2

# 哲学2

# 音楽2

# ポピュラー音楽3

# 映画2

# コメディ2

# 国花2

# 世界遺産2

# 祝祭日2

# スポーツ2

# サッカー3

# クリケット3

# 競馬3

# モータースポーツ3

# 野球3

# カーリング3

# 自転車競技3

# 脚注1

# 関連項目1

# 外部リンク1
