# coding: utf-8
import sys
import re

path = sys.argv[1]
# ファイルのパス

pattern = re.compile(r'''
    (?:File|ファイル)   # 'File'か'ファイル'どっちかにマッチすればOK
    :   # File: か ファイル: が画像なので':'もいるよね
    (.+?)   # キャプチャ対象、任意の文字1文字以上、非貪欲マッチとやら
    \|   # エスケープ
    ''', re.VERBOSE)
# 空白やコメントを正規表現パターンから除外

with open(path, 'r') as File1:
    ReadFile = File1.readlines()
    # print(ReadFile)
    for word in ReadFile:
        splitedWord = word.split('\n')
        # 改行を消す
        splitedWord = ''.join(splitedWord)

        a = ''

        a = re.findall(pattern, splitedWord)
        a = ''.join(a)
        # print(a)

        if len(a) != 0:
            print(a)

        # if a is not None:
        #     #     # Noneのもの（カテゴリーじゃないもの）は要らないので、ここで判定
        #     Word = None
        #     Count = None
        #     for w in a.groups():
        #         if not '=' in w:
        #             Word = w

        #         elif '=' in w:
        #             Count = w.count('=')-1
        #             # print(Count)
        #         if Word is not None and Count is not None:
        #             print(Word+':'+'({})'.format(str(Count)))

        # python knock24.py ./knock20_result.txt


#
