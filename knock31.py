txt = './KF_neko.txt.mecab'
mapData = {}
listData = []
with open('./KF31.txt', 'w') as writeFile:
    with open(txt, 'r') as readFile:
        for text in readFile:
            # print(text)
            # \tで区切って先頭だけ見る
            listData = text.split('\t')
            # 表層形
            surface = listData[0]
            # EOSが入ってたら消す
            if surface == 'EOS\n':
                surface = ''
            # print(surface)
            # 表層形以外をバラす
            splitted = listData[-1].split(',')
            # EOSが入ってたら消す
            if splitted == 'EOS\n':
                continue
            else:
                # 品詞
                pos = splitted[0]
                if pos in ('動詞'):
                    dousiSurface = surface
                    writeFile.write(dousiSurface+'\n')
