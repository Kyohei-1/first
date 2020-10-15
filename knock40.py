# coding: utf-8

# 40. 係り受け解析結果の読み込み（形態素）
# 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．


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

# 行頭文字判定


def first_character_decision(data):
    # 行頭文字判定タプル
    decision_candidates = ('*', "'", 'n')

    if not data.startswith(decision_candidates):
        return data

# \tで区切って表層系などに分ける


def split_t_and_parse(data):
    splitted_data = data.split('\t')
    # =====表層系=====
    surface = splitted_data[0]
    # =====表層系以外=====
    splitted_data = splitted_data[-1].split(',')
    # =====原型（基本形）=====
    base = splitted_data[6]
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


document = []  # 文全体を入れるリスト
sentence = []  # EOS区切りの異聞を入れるリスト

# ファイルのパスを格納
path = './data/ai.ja.txt.parsed'
# 読み込みでファイルを開いとく
with open(path, 'r') as read_data:
    # 1文がread_textに入る
    for read_text in read_data:
        # *,',nが先頭じゃなければdataにそのまま
        data = first_character_decision(read_text)
        # print(data)
        if data:  # None typeで無いなら
            if not data.startswith('EOS'):  # 先頭がEOSで無いなら
                # print(data)  # 1単語ごとの結果が表示される
                parsed_data = split_t_and_parse(data)
                # 1行のデータを格納
                # print(parsed_data)
                # morph = Morph(parsed_data)
                # print(parsed_data)
                morph = Morph(parsed_data)
                # print(morph)
                sentence.append(morph)
            else:
                # 先頭がEOSなら
                sentence.append(parsed_data)
                # print((sentence))
                # print(sentence)
                sentence = []
                document.append(sentence)

                # sentence.append(data)  # そこまでの結果を入れる
                # data = []
                # 全て読み終わったら
                # document.append(sentence)
    # for text in document:
    #     print(text)
    # print(document)
    # print(sentence)

    # for sentence in document:
    #     for morph in sentence:
    #         print(morph)
    #   # morph = Morph(data)
    # print(data)
    # else: #行頭がEOSならそこまでを一文とする
    #   print('ELSE')
