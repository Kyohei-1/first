# coding: utf-8
import numpy as np
import re
from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib
# txt = './KF_neko.txt.mecab'
mapData = {}
listData = []
resultList = []
word = ''
j = 0
x = []
y = []
with open('./KF36.txt', 'w') as writeFile:
    with open('./KF35-tmp.txt', 'r') as readTmpFile:
        word = readTmpFile.read()
        listWord = word.split()
        # print(listWord)

        c = Counter(listWord)
        # print(c)
        print(c.most_common(10), file=writeFile)
        result = c.most_common(10)
        # print(result)

        for i, j in result:
            print(i)
            print(j)
            # print(i[0])
            # j + 1
            plt.title('グラフ')
            # plt.xlabel(i)
            # plt.ylabel(j)
            x.append(i)
            y.append(j)

        left = np.array(x)
        height = np.array(y)
        plt.bar(left, height, color="#ABCDEF", linewidth=0)
        # plt.plot(x, y)
        plt.show()
# word = words.split(',')
# word += words
# print(word)
# writeFile.write(resultList)
# # 表層形以外をバラす
# resultList.append(surface)
# if len(listData) > 1:
#     writeFile.write(str(resultList))

# print(word+':'+str(cnt))

# print(resultList)
# splitted = listData[-1].split(',')
# # EOSが入ってたら消す
# if splitted == ['EOS\n']:
#     continue
# else:
#     # 原型（基本形）
#     base = splitted[6]
#     # 品詞
#     pos = splitted[0]
#     # 品詞細分類
#     pos1 = splitted[1]
#     mapData = {
#         'surface': surface,
#         'base': base,
#         'pos': pos,
#         'pos1': pos1
#     }
#     writeFile.write(str(mapData)+'\n')
