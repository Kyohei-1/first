txt = './KF_neko.txt.mecab'
mapData = {}
listData = []
with open('./KF30.txt', 'w') as writeFile:
    with open(txt, 'r') as readFile:
        for text in readFile:
            # print(text)
            # \tで区切って先頭だけ見る
            listData = text.split('\t')
            # 表層形
            surface = listData[0]
            # EOSが入ってたら消す
            if surface == ['EOS\n']:
                surface = ''
            # print(surface)
            # 表層形以外をバラす
            splitted = listData[-1].split(',')
            # EOSが入ってたら消す
            if splitted == ['EOS\n']:
                continue
            else:
                # 原型（基本形）
                base = splitted[6]
                # 品詞
                pos = splitted[0]
                # 品詞細分類
                pos1 = splitted[1]
                mapData = {
                    'surface': surface,
                    'base': base,
                    'pos': pos,
                    'pos1': pos1
                }
                writeFile.write(str(mapData)+'\n')
