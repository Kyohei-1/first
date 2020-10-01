# coding: utf-8

class Morph:
    def __init__(self, data):
        self.surface = data["surface"]
        self.base = data["base"]
        self.pos = data["pos"]
        self.pos1 = data["pos1"]



# ファイルのパスを格納
path = '/Users/kyohei/Desktop/100knock/data/ai.ja.txt.parsed'
# 読み込みでファイルを開いておく
with open(path, 'r') as read_data:
    # 1行ずつ拾っていく
    for read_text in read_data:
        # 以下、startswithで先頭文字を判定し、不必要そうなものを排除
        if not read_text.startswith('*'):
            if not read_text.startswith("'"):
                if not read_text.startswith('n'):
                    if not read_text.startswith('EOS'):
                        # \tで区切って先頭だけ見る
                        tmp = read_text.split('\t')
                        # =====表層系=====
                        surface = tmp[0]
                        # 表層系以外
                        splitted = tmp[-1].split(',')
                        # =====原型（基本形）=====
                        base = splitted[6]
                        # =====品詞=====
                        pos = splitted[0]
                        # =====品詞細分類=====
                        pos1 = splitted[1]
