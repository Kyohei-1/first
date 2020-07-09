# coding: utf-8
import sys
import re

path = sys.argv[1]
# ファイルのパス

with open('./KF23.txt', 'w') as wFile:
    with open(path, 'r') as File1:
        ReadFile = File1.readlines()
        # print(ReadFile)
        for word in ReadFile:
            splitedWord = word.split('\n')
            # 改行を消す
            splitedWord = ''.join(splitedWord)

            # print(splitedWord)

            # print(a)

            pattern = r'(=+)\s*([^=\s]+)\s*=+'

            a = ''

            a = re.match(pattern, splitedWord)
            print(a)
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
                    if Word is not None and Count is not None:
                        wFile.write(Word+':'+'{}'.format(str(Count))+'\n')

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

            # python knock23.py

# 実行結果
# 国名 1
# 歴史 1
# 地理 1
# 主要都市 2
# 気候 2
# 政治 1
# 元首 2
# 法 2
# 内政 2
# 地方行政区分 2
# 外交・軍事 2
# 経済 1
# 鉱業 2
# 農業 2
# 貿易 2
# 不動産 2
# エネルギー政策 2
# 通貨 2
# 企業 2
# 通信 3
# 交通 1
# 道路 2
# 鉄道 2
# 海運 2
# 航空 2
# 科学技術 1
# 国民 1
# 言語 2
# 宗教 2
# 婚姻 2
# 移住 2
# 教育 2
# 医療 2
# 文化 1
# 食文化 2
# 文学 2
# 哲学 2
# 音楽 2
# ポピュラー音楽 3
# 映画 2
# コメディ 2
# 国花 2
# 世界遺産 2
# 祝祭日 2
# スポーツ 2
# サッカー 3
# クリケット 3
# 競馬 3
# モータースポーツ 3
# 野球 3
# カーリング 3
# 自転車競技 3
# 脚注 1
# 関連項目 1
# 外部リンク 1
