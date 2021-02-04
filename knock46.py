# coding: utf-8
##########################################################
# 問題文
##########################################################
"""
46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．
項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「ジョン・マッカーシーはAIに関する最初の会議で人工知能という用語を作り出した。」という例文を考える． この文は「作り出す」という１つの動詞を含み，
「作り出す」に係る文節は「ジョン・マッカーシーは」，「会議で」，「用語を」であると解析された場合は，次のような出力になるはずである．
作り出す	で は を	会議で ジョンマッカーシーは 用語を
"""
##########################################################
# ライブラリのインポートなど
##########################################################
import re
from tqdm import tqdm


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


def sort_kaku_kou(kaku_data, kou_data):
    # kaku_data = ['は', 'で', 'を']
    # kou_data = ['ジョン・マッカーシーは', '会議で', '用語を']
    dic_list = []
    # i = 1
    kaku = []
    kou = []
    for item1, item2 in zip(kaku_data, kou_data):
        dic_list.append({
            'kaku': item1,
            'kou': item2
        })
    # print(dic_list)

    sorted_data = sorted(dic_list, key=lambda x: x['kaku'])

    kaku = [chunk_dict["kaku"] for chunk_dict in sorted_data]
    kou = [chunk_dict["kou"] for chunk_dict in sorted_data]
    #
    # for data1 in sorted_data:
    #     # print(data1)
    #     for data2 in data1.values():
    #         if i % 2 == 0:
    #             kou.append(data2)
    #             i += 1
    #         else:
    #             kaku.append(data2)
    #             i += 1

    return kaku, kou


##########################################################
# 初期化やテキストの指定
##########################################################

# 読み込むテキスト
path = '../Data/ai.ja.txt.parsed'
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
    for line in tqdm(read_file):
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
            # chunkに入れる前に記号を除去
            if parsed_data['pos'] != '記号':
                # chunkに突っ込みます
                chunk.morphs.append(morph)

##########################################################
# 出来たものを読んでいく
##########################################################
# 動詞入れる
dousi = ''
# 助詞を入れるためのもの（sortするしね）
zyosi = []
chu = []
with open('../OutputData/sortBefore.txt', 'w') as SB:
    with open('../OutputData/sortAfter.txt', 'w') as SA:
        with open('../OutputData/KF46.txt', 'w') as KF46:
            for sentence in tqdm(document):
                for chunk in sentence:
                    for morph in chunk.morphs:
                        # posはmorph.pos
                        # surfaceはmorph.surface
                        # 動詞（述語）をGet
                        if morph.pos == '動詞':
                            # 動詞を見つけたら、動詞を含むChunkに係っているChunkの助詞を見つけてくる
                            # 動詞を入れる
                            dousi = morph.base
                            # 毎回綺麗にしておく
                            chu = []
                            # print(morph.base,chunk.srcs,sep='\t')
                            for srcs in chunk.srcs:
                                for tmp in sentence[srcs].morphs:
                                    if tmp.pos == '助詞':
                                        # 助詞のリストに入れる
                                        zyosi.append(tmp.base)
                                        print(zyosi, file=SB)
                                        # zyosi.sort()
                                        print(zyosi, file=SA)
                                        # 内包表記でsurfaceを順番に取ってくる
                                        chu.append(''.join(k.surface for k in sentence[srcs].morphs))

                            kaku, kou = sort_kaku_kou(zyosi, chu)
                            if len(chu) > 0:
                                print(dousi, ' '.join(kaku), ' '.join(kou), sep='\t', file=KF46)
                            # 助詞を並べられた
                            # print(zyosi)
                            zyosi = []
                            # 動詞並べられた。
                            # print(chu)
                            # print(dousi, "\t", zyosiText, ' '.join(chu), file=KF46)
