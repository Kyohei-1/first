# coding: utf-8
##########################################################
# 問題文
##########################################################
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
##########################################################
# ライブラリのインポートなど
##########################################################
import re


##########################################################
# クラス
##########################################################

class Morph:
    def __init__(self, data):
        # 表層形
        self.surface = data['surface']
        # 基本形
        self.base = data['base']
        # 品詞
        self.pos = data['pos']
        # 品詞細分類
        self.pos1 = data['pos1']

    def __repr__(self):
        # これがないと、オブジェクトの値？が表示される？だった気がする
        # 使うのはbaseだと思うので変えといた
        return "base:{}".format(self.base)

    # 　morphのposが指定した品詞かどうか判定する関数
    def is_particle(morph, choice):
        return morph.pos == choice


class Chunk:
    def __init__(self, chunk_id, dst):
        # 自分自身の文節番号
        self.chunk_id = chunk_id
        # 文節が係っている相手の文節番号
        self.dst = dst
        # 自分の文節に係っている相手の文節番号
        self.srcs = []
        # Morphを突っ込むやつ（雑な紹介）
        self.morphs = []

    def __repr__(self):
        # 山下氏に教えてもらったやつ Chunkの中の要素を返す関数って認識
        return "chunk_id: {}\ndst: {}\nmorphs: {}\nsrcs: {}\n".format(self.chunk_id, self.dst,
                                                                      "".join([morph.surface for morph in self.morphs]),
                                                                      self.srcs)


##########################################################
# 関数
##########################################################

def debug(data):
    print(data)
    print(type(data))
    exit()


# \tで区切って表層形などに分ける関数
def split_t_and_parse(data):
    splitted_data = data.split('\t')
    # 表層形(surface)
    surface = splitted_data[0]
    # 行末の改行を殺す
    surface = surface.rstrip('\n')
    # 表層形以外のもの
    splitted_data = splitted_data[-1].split(',')
    # 原型（基本形）(base)
    base = splitted_data[6]
    if base == '*\n':
        base = base.replace('\n', '')
    # 品詞(pos)
    pos = splitted_data[0]
    # 品詞細分類(pos1)
    pos1 = splitted_data[1]
    parsed_data = {
        'surface': surface,
        'base': base,
        'pos': pos,
        'pos1': pos1
    }
    return parsed_data


# 行頭判定
def line_head_judgment(data, text):
    return data.startswith(text)


##########################################################
# 初期化やテキストの指定
##########################################################

# 読み込むテキスト
path = 'ai.ja.txt.parsed'
# 初期化的な何か
sentence = []
document = []
# 最初が中身空になるから書いていた記憶がある
chunk = Chunk('dummy', 'dummy')
# chunk_id保管用
chunk_id_list = []
# dst保管用
dst_list = []
# chunkのインデックス番号を入れる
chunk_index = ''
##########################################################
# データを作るまで
##########################################################

# ファイル読み込み
with open(path, 'r') as read_file:
    # 1行読み込む
    for line in read_file:
        # 行頭が*
        if line_head_judgment(line, '*'):
            # print('*ルート')
            # debug(line)
            # morphsが作られているなら
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
            # chunkを作る
            chunk = Chunk(chunk_id, dst)

        # 行頭がEOS
        elif line_head_judgment(line, 'EOS'):
            # print('EOSルート')
            # debug(line)
            # chunk_idとdstがdummyじゃない場合
            if chunk.chunk_id != 'dummy' or chunk.dst != 'dummy':
                # chunkをsentenceに入れる
                sentence.append(chunk)

            # インデックス番号と要素の中身を取得
            for chunk_index, chunk in enumerate(sentence):
                # TODO: 説明できないのでやり直す
                sentence[chunk.dst].srcs.append(chunk_index)

            # sentenceをdocumentに入れる
            document.append(sentence)
            # また使うものを初期化
            sentence = []
            chunk_id_list = []
            dst_list = []
            chunk = Chunk("dummy", "dummy")

        # 行頭が文字
        else:
            # print('Otherルート')
            # debug(line)
            # 品詞を分ける
            parsed_data = split_t_and_parse(line)
            # debug(parsed_data)
            # morphを作る
            morph = Morph(parsed_data)
            # chunkに入れる
            chunk.morphs.append(morph)

##########################################################
# 出来たものを読んでいく
##########################################################
dousi = []
zyosi = []
result = []
with open('./KF45.txt', 'w') as KF45:
    for sentence in document:
        for chunk in sentence:
            for morph in chunk.morphs:
                # posはmorph.pos
                # surfaceはmorph.surface
                # 動詞（述語）をGet
                if morph.pos == '動詞':
                    dousi.append(morph.surface)
                elif morph.pos == '助詞':
                    zyosi.append(morph.surface)

        result.append(dousi + zyosi)
        dousi, zyosi = [], []
        # print(dousi)
        # print(zyosi)

    print(result, file=KF45)
