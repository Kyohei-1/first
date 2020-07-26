# coding: utf-8
import re
from collections import Counter
# txt = './KF_neko.txt.mecab'
mapData = {}
listData = []
resultList = []
word = ''
with open('./KF36.txt', 'w') as writeFile:
    with open('./KF35-tmp.txt', 'r') as readTmpFile:
        word = readTmpFile.read()
        listWord = word.split()

        c = Counter(listWord)
        print(c.most_common(10), file=writeFile)
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
