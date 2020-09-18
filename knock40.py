# import re
# class Morph:
#     # コンストラクタ
#     def __init__(self, surface, base, pos, pos1):
#         self.surface = surface
#         self.base = base
#         self.pos = pos
#         self.pos1 = pos1
#     # シンプルに値を返すだけに使うメソッド

#     def getValue(self):
#         return self.surface, self.base, self.pos, self.pos1


# path = './ai.ja.txt.parsed'
# with open(path, 'r') as readFile:
#     text = readFile.read().split()
#     result = []
#     morphs = []
#     for line in text[:-1]:
#         # print(line)
#         if line == 'EOS':
#             result.append(morphs)
#             morphs = []
#         elif line[0] == '*':
#             continue
#         else:
#             ls = line.split('\t')
#             d = {}
#             tmp = ls[0].split(',')
#             morph = Morph(ls[0], tmp[6], tmp[0], tmp[1])
#             morphs.append(morph)
#     for morphs in result[2]:
#         print(morphs.getValue())

import re

morphs = []
sentences = []

# 区切り文字
separator = re.compile('\t|,')

# 除外行
exclude = re.compile(r'''EOS\n      # EOS, 改行コード
                         |          # OR
                         \*\s\d+\s  # '*, 空白, 数字１つ以上, 空白
                       ''', re.VERBOSE)
# 正規表現の中身は調べて出てきたものをコピペした


class Morph:
    def __init__(self, line):

        # タブとカンマで分割
        cols = separator.split(line)
        # print(cols)

        self.surface = cols[0]  # 表層形(surface)
        # print(cols[0])
        self.base = cols[7]    # 基本形(base)
        # print(cols[7])
        self.pos = cols[1]     # 品詞(pos)
        # print(cols[1])
        self.pos1 = cols[2]    # 品詞細分類1(pos1)
        # print(cols[2])


# ファイルを開く
with open('./ai.ja.txt.parsed', 'r') as f:

    # fからlineで1行分取り出す
    for line in f:
        # print(line)
        # 必要でない行は無視（正規表現にハマるものは不必要）
        if not exclude.match(line):
            # print(line)
            # morphというリストに値を入れる
            # Morphクラスを経由
            morphs.append(Morph(line))

        if line == 'EOS\n' and len(morphs) > 0:
            sentences.append(morphs)
            # morphs = []

for sentence in sentences[1]:
    print(sentence.__dict__)
