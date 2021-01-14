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

# \tで区切って表層形などに分ける関数
def split_t_and_parse(data):
    splitted_data = data.split('\t')
    # 表層形(surface)
    surface = splitted_data[0]
    # 行末の改行を殺す
    if surface == '*':
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


# 　morphのposが指定した品詞かどうか判定する関数
def is_particle(morph, choice_pos):
    return morph.surface == choice_pos


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

# ファイル読み込み
with open(path, 'r') as read_file:
    # 1行読み込む
    for line in read_file:
        # 行頭が*
        if line_head_judgment(line, '*'):
            print('T')
        # 行頭がEOS
        if line_head_judgment(line,'EOS'):
            print('F')
        # 行頭が文字
        else:
            # 品詞を分ける
            parsed_data = split_t_and_parse(line)
            # morphを作る
            morph = Morph(parsed_data)
            # chunkに入れる
            chunk.morphs.append(morph)



