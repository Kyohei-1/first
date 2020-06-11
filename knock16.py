# coding: utf-8
import sys

line = int(sys.argv[1])
# 行数

path = sys.argv[2]
# ファイルのパス

with open(path, 'r') as r_File:
    lines = len(r_File.readlines())
    lines_str = r_File.read()
    # 行数を取得
    print(lines)
    print(r_File.readlines())


# 同じ量を全員に配るとすると、もらえる量は
div = lines // line  # 2780 // 97 = 28
print(div)
# 同じ量を全員に配った後のあまりを求める
rem = lines % line  # 2780 % 97 = 64
print(rem)
# n人中rem人は余りをひとつずつもらえる
l = [div] * (line - rem) + [div+1] * rem

print(l)

i = 1
for word in lines_str:
    fileName = "knock16-{:02d}.txt".format(i)
    # ファイル名をかぶらないように作成
    for line in lines_str[i:l[i]]:
        fileName.write(line)
        i += 1

        # TODO 面倒だったので、後回し。
        # python knock16.py 100 ./popular-names.txt
