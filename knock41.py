# coding: utf-8

import re
import knock40

# 41. 係り受け解析結果の読み込み（文節・係り受け）Permalink
# 40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストの係り受け解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，冒頭の説明文の文節の文字列と係り先を表示せよ．本章の残りの問題では，ここで作ったプログラムを活用せよ．


class Chunk:
    def __init__(self, chunk_id, dst, morph):

        self.morph = []  # Morphオブジェクトのリスト
        self.dst = dst  # 係り先文節インデックス番号
        self.srcs = []  # 係り元文節インデックス番号のリスト


class Morph:
    def __init__(self, data):
        self.surface = data['surface']  # 表層形
        self.base = data['base']  # 基本形
        self.pos = data['pos']  # 品詞
        self.pos1 = data['pos1']  # 品詞細分類1

    def __repr__(self):
        return "surface:{}\tbase:{}\tpos:{}\tpos1:{}".format(
            self.surface, self.base, self.pos, self.pos1
        )


# 文節を判断するフラグ
# 最初はTrueで、行頭が「*」以外だとFalseにする
judgement_flag = True

# 入れとくリスト
sentence = []

with open('./ai.ja.txt.parsed-min') as read_file:
    for line in read_file:
        # 先頭がEOSで無いなら
        if not line.startswith('EOS'):
            # 解析結果がある行はこっち
            if line.startswith('*'):
                # 行頭が文字ではない→「*」である→新たな行頭が来たという判断
                if judgement_flag == False:
                    # Chunk(chunk_id, dst, morphs) を作ってsentenceリストにappend
                    sentence.append(Chunk(chunk_id, dst, morph))

                judgement_flag = True
                # \tと半角空白で分割する
                splitted = re.split('[\t, ]', line)
                # 文節番号入れとく
                chunk_id = splitted[1]
                # 一つ前の文節番号と比較して同じもしくは小さくなっている場合
                # 文節が変わっている
                dst = splitted[2].rstrip('D')  # 係り先番号入れる

            else:  # 文字がある方はこっち
                judgement_flag = False
                parsed_data = knock40.split_t_and_parse(line)
                # morphオブジェクト作るやで
                morph = Morph(parsed_data)
        # 行頭がEOSならば文の終わりなので係り元を埋める
        # else:
print(sentence)
