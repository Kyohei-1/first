# # coding: utf-8
# pathにMeCabのデータを放り込む
path = './KF_neko.txt.mecab'

# ファイルを読み込みで開くやで
with open(path, 'r') as readFile:
    for readData in readFile:
        readData = readData.split('\t')
        # print(readData[0])
        surface = readData[0]  # 表層型
        # if surface == 'EOS\n':
        #     print('')
        # else:
        #     print(surface)
        print(readData[1])
        # splitedData = readData[1].split(',')
        # TODO EOS\nをどうやって殺すか
        # print(splitedData[1])
        # pos = splitedData[0]  # 品詞
        # pos1 = splitedData[1]  # 品詞細分類１
        # pos2 = splitedData[2]  # 品詞細分類２
        # pos3 = splitedData[3]  # 品詞細分類３
        # practice = splitedData[4]  # 活用型
        # inflectional = splitedData[5]  # 活用形
        # base = splitedData[6]  # 基本形（原形）
        # reading = splitedData[7]  # 読み
        # pronounce = splitedData[8]  # 発音

        # # print(base)
        # # print(reading)
        # # print(pronounce)
