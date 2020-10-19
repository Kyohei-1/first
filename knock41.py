# coding: utf-8

import re
# また書くの面倒だからね
import knock40

# 41. 係り受け解析結果の読み込み（文節・係り受け）Permalink
# 40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストの係り受け解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，冒頭の説明文の文節の文字列と係り先を表示せよ．本章の残りの問題では，ここで作ったプログラムを活用せよ．


class Chunk:
    def __init__(self, dst):

        self.morphs = []  # Morphオブジェクトのリスト
        self.dst = dst  # 係り先文節インデックス番号
        self.srcs = []  # 係り元文節インデックス番号のリスト


text_path = './data/ai.ja.txt.parsed'
start_with_asterisk = []
start_with_other = []
# 文節番号を入れるリスト
clause_number = []
# 係り先番号を入れるリスト
clerk_target_number = []

with open(text_path, 'r') as read_data:
    for read_text in read_data:
        if read_text.startswith('*'):
            read_text = read_text.rstrip('\n')
            # \tと半角空白で区切る
            read_text = re.split('[\t, ]', read_text)
            read_text = read_text
            clause_number.append(read_text[1])  # 文節番号
            clerk_target_number.append(read_text[2].rstrip('D'))  # 係り先番号

            # print(start_with_asterisk)
        else:  # * じゃない行はこっち
            # print(read_text)
            read_text = re.split('[\t, ]', read_text)
            print(read_text[0])
            # start_with_other.append(read_text.strip())
            # start_with_other = start_with_other.split(',')
            # print(start_with_other[6])
# print(clerk_target_number)
# print(clause_number)
