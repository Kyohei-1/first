txt = './KF_neko.txt.mecab'
mapData = {}
listData = []
tmpText1 = '2020'
tmpText2 = '2020'
tmpText3 = '2020'
counter = 0
tmpText_flg1 = False
tmpText_flg2 = False
tmpText_flg3 = False

with open('./KF33.txt', 'w') as writeFile:
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
                # 前の分が名詞「一般」なら取得
                pos = splitted[0]
                pos1 = splitted[1]

                if tmpText_flg1 and tmpText_flg2 == True:
                    if pos in '名詞' and pos1 in '一般' or pos1 in '代名詞':
                        tmpText3 = text[0]
                        tmpText_flg3 = True
                        if tmpText_flg3:
                            writeFile.write(tmpText1+tmpText2 +
                                            tmpText3+'\n')

                if pos in '名詞' and pos1 in '一般' or pos1 in '代名詞':
                    tmpText1 = text[0]
                    tmpText_flg1 = True
                    # print(tmpText1)
                if pos in '助詞' and pos1 in '連体化':
                    tmpText2 = text[0]
                    tmpText_flg2 = True

                    # if '2020' not in tmpText1 and '2020' not in tmpText2 and '2020' not in tmpText3:
                    #     writeFile.write(tmpText1+tmpText2+tmpText3+'\n')
                # # 恐らく助詞で連体化の「の」を取ってくればいい
                # # その前と後ろを含めて取得
                # if pos in ('助詞'):
                #     # writeFile.write('SUCCESS')
                #     if pos1 in ('連体化'):
                #         # writeFile.write('SUCCESS2')
                #         # 助詞で連体化の「の」
                #         prevMeisi = splitted[5]
                #         zyosiRentai = splitted[6]
                #         nextMeisi = splitted[7]
                #         zyosiRentai = prevMeisi+nextMeisi
                #         writeFile.write(zyosiRentai+'\n')
