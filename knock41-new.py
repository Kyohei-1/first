# coding: utf-8

import re


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


class Chunk:
    def __init__(self, chunk_id, dst):

        self.chunk_id = chunk_id  # 文節番号
        self.morph = []  # Morphオブジェクトのリスト
        self.dst = dst  # 係り先文節インデックス番号
        self.srcs = []  # 係り元文節インデックス番号のリスト

    def __repr__(self):
        return "{}\tmorph:{}dst:{}\t".format(
            self.chunk_id, self.morph, self.dst)

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

    # print('surface:'+surface)
    # print('base:'+base)
    # print('pos:'+pos)
    # print('pos1:'+pos1)

    parsed_data = {
        'surface': surface,
        'base': base,
        'pos': pos,
        'pos1': pos1
    }

    return parsed_data


# chunkを入れとくリスト
sentence = []
# sentenceを入れとくリスト
document = []
# 読み込むテキスト
path = './ai.ja.txt.parsed-min'

# ファイルを読み込む
with open(path, 'r') as read_file:
        # 1行読み込む
    for line in read_file:
        # *で始まったなら
        if line.startswith('*'):
            # \tと半角空白でsplit
            splitted = re.split('[\t ]', line)
            # 文節番号
            chunk_id = splitted[1]
            # 係り先番号
            dst = splitted[2].rstrip('D')
            # chunkを作る（chunk_idとdstを入れる）
            chunk = Chunk(chunk_id,dst)

        # 行頭がEOS
        elif line.startswith('EOS'):
            # chunkをsentenceに入れる
            sentence.append(chunk)
            # sentenceをdocumentに入れる
            document.append(sentence)

        # 行頭が*でもEOSでも無い場合
        else:
            # バラします
            parsed_data = split_t_and_parse(line)
            # morphを作ります
            morph = Morph(parsed_data)
            # chunkに突っ込みます
            chunk.morph = morph

print(document)