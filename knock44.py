# coding: utf-8

import re
# from graphviz import Graph
# from graphviz import Digraph
from tqdm import tqdm
import pydot

# import pydoc


class Morph:
    def __init__(self, data):
        self.surface = data['surface']  # 表層形
        self.base = data['base']  # 基本形
        self.pos = data['pos']  # 品詞
        self.pos1 = data['pos1']  # 品詞細分類1

    def __repr__(self):
        return "surface:{}".format(self.surface)


class Chunk:
    def __init__(self, chunk_id, dst):
        self.chunk_id = chunk_id  # 文節番号
        self.dst = dst  # 係り先文節インデックス番号
        self.srcs = []  # 係り元文節インデックス番号のリスト
        self.morphs = []  # Morphオブジェクトのリスト

    def __repr__(self):
        return "chunk_id: {}\ndst: {}\nmorphs: {}\nsrcs: {}\n".format(self.chunk_id, self.dst,
                                                                      "".join([morph.surface for morph in self.morphs]),
                                                                      self.srcs)


# \tで区切って表層系などに分ける
def split_t_and_parse(data):
    splitted_data = data.split('\t')
    # =====表層系=====
    surface = splitted_data[0]
    # 行末の改行を殺す
    if surface == '*':
        surface = surface.rstrip('\n')

    # =====表層系以外=====
    splitted_data = splitted_data[-1].split(',')
    # =====原型（基本形）=====
    base = splitted_data[6]
    if base == '*\n':
        base = base.replace('\n', '')
    # =====品詞=====
    pos = splitted_data[0]

    # =====品詞細分類=====
    pos1 = splitted_data[1]

    parsed_data = {
        'surface': surface,
        'base': base,
        'pos': pos,
        'pos1': pos1
    }

    return parsed_data


# 読み込むテキスト
path = 'ai.ja.txt.parsed-min'
# 初期化
sentence = []
document = []
chunk = Chunk("dummy", "dummy")
chunk_id_list = []
dst_list = []

# ファイルを読み込む
with open(path, 'r') as read_file:
    # 1行読み込む
    for line in read_file:
        # *で始まったなら
        if line.startswith('*'):
            # 有効なchunkなら
            if len(chunk.morphs) > 0:
                # chunkをsentenceに入れる
                sentence.append(chunk)

            # \tと半角空白でsplit
            splitted = re.split('[\t ]', line)
            # 文節番号
            chunk_id = int(splitted[1])
            chunk_id_list.append(chunk_id)
            # 係り先番号

            dst = int(splitted[2].rstrip('D'))
            dst_list.append(dst)

            # chunkを作る（chunk_idとdstを入れる）
            chunk = Chunk(chunk_id, dst)

        # 行頭がEOS
        elif line.startswith('EOS'):
            if chunk.chunk_id != 'dummy' or chunk.dst != 'dummy':
                # chunkをsentenceに入れる
                sentence.append(chunk)

            # enumerateでインデックス番号と中身？（要素）をそれぞれ取得
            for chunk_index, chunk in enumerate(sentence):
                # chunk_indexは文節番号 chunkはチャンク
                # chunkのdst（係り先が-1でなければ）
                if chunk.dst != -1:
                    if chunk.dst != 'dummy':
                        # sentence > chunkなので
                        # sentenceというかリストの中のdst番目の場所にアクセスする
                        # sentence.chunk.dstと書くとエラーになる（リストだから）
                        # 文節番号を係り先のリストのsrcsに入れとく
                        sentence[chunk.dst].srcs.append(chunk_index)

            # sentenceをdocumentに入れる
            document.append(sentence)
            # 初期化
            sentence = []
            chunk_id_list = []
            dst_list = []
            chunk = Chunk("dummy", "dummy")

        # 行頭が*でもEOSでも無い場合
        else:
            # バラします
            parsed_data = split_t_and_parse(line)
            # morphを作ります
            morph = Morph(parsed_data)
            if parsed_data['pos'] != '記号':
                # chunkに突っ込む
                chunk.morphs.append(morph)

# for sentence in document:
#     for chunk in sentence:
#         print(chunk)
# print("===EOS===")

# ペアを入れる配列を用意
pairs = []
count = 0
for sentence in tqdm(document):
    count += 1
    for chunk in sentence:
        for morph in chunk.morphs:
            # posが記号以外ならchunk.morphsを
            # ifのみに修正→elseを用いない場合、後ろにifを書くらしい。前に書くとsyntax error
            a = ''.join([b.surface for b in chunk.morphs if b.pos != '記号'])
            b = ''.join([b.surface for b in sentence[int(chunk.dst)].morphs if b.pos != '記号'])
            a_p = [b.pos for b in chunk.morphs]
            b_p = [b.pos for b in sentence[int(chunk.dst)].morphs]
            # # 係り元に名詞が含まれて、かつ、係り先に動詞があるものを表示します
            if '名詞' in a_p and '動詞' in b_p:
                # print(a, b, sep='\t')
                # ここから追記
                c = a, b
                pairs.append(c)
            n = pydot.Node('node')
            n.fontname = 'IPAGothic'
            graph = pydot.graph_from_edges(pairs, directed=True)
            graph.add_node(n)
            graph.write_png('./output.png')
