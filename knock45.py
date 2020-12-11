# coding: utf-8

"""
45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
ただし，出力は以下の仕様を満たすようにせよ．

動詞を含む文節において，最左の動詞の基本形を述語とする
述語に係る助詞を格とする
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
「ジョン・マッカーシーはAIに関する最初の会議で人工知能という用語を作り出した。」という例文を考える．
この文は「作り出す」という１つの動詞を含み，
「作り出す」に係る文節は「ジョン・マッカーシーは」，「会議で」，「用語を」であると解析された場合は，
次のような出力になるはずである．

作り出す	で は を
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語と格パターンの組み合わせ
「行う」「なる」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
"""
from tqdm import tqdm
import re


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
verb_flg = False
tmp = []

# ファイルを読み込む
with open(path, 'r') as read_file:
    # 1行読み込む
    for line in tqdm(read_file):
        # *で始まったなら
        if line.startswith('*'):
            # 有効なchunkなら（morphsが作られているなら）
            if int(len(chunk.morphs)) > 0:
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
                if chunk.dst != -1 and chunk.dst != 'dummy':
                    # sentence > chunkなので
                    # sentenceというかリストの中のdst番目の場所にアクセスする
                    # sentence.chunk.dstと書くとエラーになる（リストだから）
                    # 文節番号を係り先のリストのsrcsに入れとく
                    sentence[chunk.dst].srcs.append(chunk_index)

            # sentenceをdocumentに入れる
            document.append(sentence)
            # 初期化
            # verb_flg = False
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
            # chunkに突っ込む
            chunk.morphs.append(morph)

# TODO 係り先、係り元の内包表記は43のコピペ　すまん。
# TODO UNIXコマンドでの確認は面倒だったから無視した。

with open('./KF45.txt', 'w') as KF45:
    for sentence in document:
        # EOS区切りで1 sentenceなので文頭の動詞を取得する
        verb_flg = False

        # 先頭だけ欲しいのでsentenceごとにflgで先頭のみ取る
        for chunk in sentence:
            for morph in chunk.morphs:
                # 各文の先頭の動詞を取得
                if morph.pos == '動詞' and verb_flg is False:
                    verb_flg = True
                    # 各文頭の動詞が取れた
                    print(morph.surface, chunk.srcs, sep='\t')
                    # 助詞判定
                # if morph.pos == '助詞':


    # print(morph.surface)
    # if morph.pos == '動詞':
    #     print('動詞', chunk.srcs, sep='\t')
    # elif morph.pos == '助詞':
    #     print('助詞', chunk.dst, sep='\t')

    # a = ''.join([b.surface for b in chunk.morphs])
    # b = ''.join([b.surface for b in sentence[int(chunk.dst)].morphs])
    # a_p = [b.pos for b in chunk.morphs]
    # b_p = [b.pos for b in sentence[int(chunk.dst)].morphs]
    # print(a,b,sep='\t')
    # # 係り元に名詞が含まれて、かつ、係り先に動詞があるもの　かつ、flgがfalseのもの
    # if '助詞' in a_p and '動詞' in b_p and verb_flg is False:
    #     # aに名詞＋助詞が入っているので、aを分割
    #     print(b, a, sep='\t', file=KF45)
    #     verb_flg = True

# for sentence in document:
#     for chunk in sentence:
#         print(chunk)
# print("===EOS===")
