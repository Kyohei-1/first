# coding: utf-8
##########################################################
# 問題文
##########################################################
"""
47. 機能動詞構文のマイニングPermalink
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
46のプログラムを以下の仕様を満たすように改変せよ．
「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「また、自らの経験を元に学習を行う強化学習という手法もある。」という文から，
以下の出力が得られるはずである．
学習を行う	に を	元に 経験を
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


# 文節に サ変接続名詞 + を（助詞）が含まれているか判定
def bunsetu_check(data,first_flg,second_flg):
    for morph in data:
        if morph.pos1 == 'サ変接続':
            first_flg = True
        if morph.base == 'を':
            second_flg = True
        # print(first_flg,second_flg,sep='\t')
        if first_flg == True and second_flg == True:
            # print('All True')
            return True
        # if first_flg == True and second_flg == True:
        #     print('True')
        #     return True
        # else:
        #     print('False')
        #     return False


        # if first_flg and second_flg:
            # print('サ変＋助詞')
    # result_data = ''.join([morph.base for morph in chunk.morphs])


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
path = '../Data/ai.ja.txt.parsed-min'
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
                # print(parsed_data['surface'])
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
c_id = ''
#
first_flg = False
second_flg = False
verb_flg = False
dousi_list = []
with open('../Output/KF47.txt', 'w') as KF47:
    # open('../Output/KF47-test.txt','w') as TEST47:
    for sentence in tqdm(document):
        for chunk in sentence:
            for morph in chunk.morphs:
                # posはmorph.pos
                # surfaceはmorph.surface
                # 動詞（述語）をGet
                if morph.pos == '動詞' and verb_flg == False:
                    # 動詞を見つけたら、動詞を含むChunkに係っているChunkの助詞を見つけてくる
                    # 動詞を入れる
                    dousi = morph.base
                    # 動詞を入れる（47用）
                    dousi_list.append(morph.base)
                    # 連続しているか判断するためのchunk_id
                    c_id = chunk.chunk_id
                    # print(c_id)
                    # 毎回綺麗にしておく
                    chu = []
                    verb_flg = True
                    # print(morph.base,chunk.srcs,sep='\t')

                    for srcs in chunk.srcs:
                        for tmp in sentence[srcs].morphs:
                            if tmp.pos == '助詞':
                                if srcs == (c_id - 1):
                                    dousi_list.append(''.join(k.surface for k in sentence[srcs].morphs))
                                else:
                                    # print(tmp)
                                    # 助詞のリストに入れる
                                    zyosi.append(tmp.base)
                                    # 内包表記でsurfaceを順番に取ってくる
                                    chu.append(''.join(k.surface for k in sentence[srcs].morphs))

                    kaku, kou = sort_kaku_kou(zyosi, chu)

                    if len(chu) > 0:
                        tmp_list = dousi_list
                        dousi_list = []
                        # print(tmp_list)
                        dousi_list.append(tmp_list[1])
                        dousi_list.append(tmp_list[0])
                        tmp_list = []
                        # print(dousi_list)
                        # print(dousi_list,file=TEST47)
                        # print(dousi, ' '.join(kaku), ' '.join(kou), sep='\t', file=KF47)
                        print(''.join(dousi_list),' '.join(kaku),' '.join(kou),sep='\t',file=KF47)
                    # 助詞を並べられた
                    # print(zyosi)
                    zyosi = []
                    c_id = ''
                    # 動詞並べられた。
                    # print(chu)
                    # print(dousi, "\t", zyosiText, ' '.join(chu), file=KF46)
