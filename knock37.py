import re
from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib

txt = './KF_neko.txt.mecab'
# mapData = {}
data = ''
neko = []

with open('./KF37.txt', 'w') as writeFile:
    with open(txt, 'r') as readFile:
        # txt = readFile.read()
        # txt_list = txt.split('EOS')
        # readFile = readFile.split('EOS')
        for text in readFile:
            # text = text.split('EOS')
            # print(text)
            # \tで区切って先頭だけ見る
            listData = text.split('\t')
            # 表層形
            surface = listData[0]
            # print(surface)
            # data = data.split()
            data += surface
        data = data.split()
        data = ''.join(data)
        data = ''.join(data).split('EOS')
        for bun in data:
           # dataはlist 
           # print(type(data))
           # bunは文字列
           # print(type(bun))
           if '猫' in bun:
               # 猫が含まれている行を抽出してリストに入れる
               neko.append(bun)
               print(neko)

        # こっから下は気にしないで。#
        # print(data)
        # print(any(x is e or x == e for e in y))
        # if '猫' not in data:
             # print(data)
        # data = ''.join(data).split('EOS')
        # print(data)
        
        # data = ''.join(data)
        # if(data != ''):
        # if('猫' in data):
            # print('Cat')
