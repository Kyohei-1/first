# ファイルを結合したい
import sys
path1 = sys.argv[1]
path2 = sys.argv[2]
# いつも通りのやつ 引数を取得して入れとく
path1 = path1.strip()
path2 = path2.strip()

with open(path1, 'r') as file1, open(path2, 'r') as file2, open('./result.txt', 'w') as resultFile:
    for words1, words2 in zip(file1, file2):
        words1 = words1.rstrip()
        words2 = words2.rstrip()
        resultFile.write("{0}\t{1}\n".format(words1, words2))

# python /Users/kyohei/Desktop/100knock/knock13.py /Users/kyohei/Desktop/100knock/col1.txt /Users/kyohei/Desktop/100knock/col2.txt
