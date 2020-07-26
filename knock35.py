# coding: utf-8
import re
from collections import Counter
txt = './KF_neko.txt.mecab'
mapData = {}
listData = []
resultList = []

with open('./KF35-tmp.txt', 'w') as writeTmpFile:
    with open(txt, 'r') as readFile:
        for text in readFile:
            # print(text)
            # \tで区切って先頭だけ見る
            listData = text.split('\t')
            # 表層形
            surface = listData[0]
            # 改行、タブ、スペースなどをまとめて削除
            surface = re.sub(r"\s", "", surface)
            surface = surface.replace('。', '')
            surface = surface.replace('-', '')
            surface = surface.replace('--', '')
            surface = surface.replace('ー', '')
            surface = surface.replace('ーー', '')
            surface = surface.replace('、', '')
            surface = surface.replace(',', '')
            surface = surface.replace('　', '')
            surface = surface.replace(' ', '')
            surface = surface.replace(', ', '')
            surface = surface.replace(',　', '')
            surface = surface.replace('「', '')
            surface = surface.replace('」', '')
            surface = surface.replace('——', '')
            surface = surface.replace('一', '')

            # EOSが入ってたら消す
            if surface in 'EOS\n':
                surface = ''
            if surface in '':
                continue
            writeTmpFile.write(''.join(surface)+' ')
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
