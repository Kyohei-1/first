import re
from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib

txt = './KF_neko.txt.mecab'
mapData = {}
data = ''


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
        if '猫' in data:
            print(data)
        else:
            print('Bad')
        # data = ''.join(data).split('EOS')
        # print(data)
        
        # data = ''.join(data)
        # if(data != ''):
        # if('猫' in data):
            # print('Cat')
