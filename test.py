# -*- coding: utf-8 -*-

# kyori = 507.5
# jisoku = 80
# jikan = kyori / jisoku
# print(jikan)

# per_inch =2.54
# inch = 8
# cm = inch * per_inch
# print(cm)

# print('インチは',inch,'です')

# str = '''
# aaaaaa
# bbbbbb
# cccccc
# '''
# print(str)

# name = 'キティー'
# cm = 150
# # 文字列で説明を加える
# desc = '{0}の身長 = {1}センチ'.format(name,cm)
# print(desc)

# print('私は{name}です。'.format(name='キョーヘー'))
# print('{job1}であり、{job2}です'.format(job1='プログラマ',job2='経営者'))

# # 名前を入力
# name = input('What you are name ?\n')
# # 挨拶を表示
# print(name+'さんこんにちは！')

# per_inch = 2.54
# inch = input('inch\n')
# cm = float(inch) * per_inch
# desc = '{0}inch = {1}cm'.format(inch,cm)
# print(desc)


from random import *


def changeInt(word):
    return int(word)


def changeFloat(word):
    return float(word)


def changeStr(word):
    return str(word)

# a = 'a'
# b = 2
# c = 0
# d = '0'
# e = 3.64

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# print('給料計算')
# hourMoney = float(input('時給を入力してください\n'))
# workTime = float(input('働いた時間を入力してください\n'))
# money = hourMoney * workTime
# print('給料は',money,'円です'.format(money=money))

# year = int(input('西暦何年？'))
# is_leap = (year % 400 == 0)or((year % 100 != 0))and(year % 4 == 0)
# if is_leap:
#   print('うるう年です')
# else:
#   print('平年です')

# ene = 3
# while ene > 0:
#   print('走る')
#   ene -= 1
# print('GOAL')

# while True:
#   user = input()
#   if user == "" or user == "q": break
#   tubo = int(user)
#   m2 = tubo * 3.31
#   s = "{0}坪は {1}平方メートルです".format(tubo,m2)
#   print(s)

# for i in range(0,100):
#   print(str(i))

# from tkinter import *
# w = Canvas(Tk(), width=900, height=400)
# w.pack()

# for i in range(300):
#     x = i * 3
#     w.create_line(x,0,400,fill="#ABCDEF")
# mainloop()

# a = [10,22,30,45]
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# a[0] ='a'
# a[1] = 'b'
# a[2] = 'c'
# a[3] = 50
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(len(a))

# points = [88, 76, 67, 43, 79, 80, 91]
# # print(round(sum(points)/len(points)))
# # print(sum(points))
# # print(len(points))
# pointsSum = 0
# # # iに配列の値が順次入る→sumにiを足す
# # for i in points:
# #     sum += i
# #     print(sum)
# pointsSum = sum(points)
# print(pointsSum)


# ランダムにモンスターを格納
monster1 = ['タイラント', 'ネメシス', 'ゾンビ']
monster2 = ['フリッカー', 'ハンターα', 'ハンターγ']
# # print(len(monster))
# # monster.append('村長')
# # monster.append('ウェスカー')
# # print(len(monster))
# # Monster = monster[randint(0,int(len(monster)-1))]
# # print(Monster)
# # if not monster:
# #     print('False')
# # else:
# # print(list(enumerate(monster1+monster2)))
# #     print('Success')
# monster3 = monster1 + monster2
# print(monster1)
# print(monster2)
# print(monster3)
# print(monster1)
# print(monster1.extend(monster2))
# tup = (
#     'ポッチャマ','ヒコザル','ナエトル'
# )
# print(type(tup))
# # tupleは変更出来ないってことか
# # tup.append('アルセウス')
# print(tup)
monster1 = ['タイラント', 'ネメシス', 'ゾンビ']
monster2 = ['フリッカー', 'ハンターα', 'ハンターγ']
monster3 = monster1.append(monster2)
# print(monster1.append(monster2))
# print(monster1)
# print(monster1.extend(monster2))
# print(type(monster1))
# print(type(monster3))
# if monster3 is None:
#     print('あかんやん')

# print(monster1)
# print(monster3)
# print(monster1[0:2])

# ステップ値に-をつけると逆になる
# str[::-2]はひっくり返して2文字ごとにスライス（取り出す）
# str = 'stressed'
# str = str[::-2]
# print(str)

# del monster1
# print(monster1)

# 集合型を生成
score1 = {
    11,53,73,94,2,58,93,83,100,72
}

score2 = {
    35,83,100,83,94,2,94,82,82,95,1
}
# print(sorted(score1+score2))
# print(score3)

# print('和：'+str(score1|score2))
# print('差：'+str(score1-score2))
# print('または：'+score1^score2)
# print('かつ：'+score1&score2)

age = {
    '鈴木':30,'井上':45,'佐藤':60
}

print(sorted(age.keys()))
print(sorted(age.values()))