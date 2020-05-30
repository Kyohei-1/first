# -*- coding: utf-8 -*-
# 実行する際はpython3で実行してね

# Q0
# string = 'stressed'
# string = string[::-1]
# print (string)

# Q1
# str = '「パタトクカシーー」'
# print(str[1]+str[3]+str[5]+str[7])


# Q2
# .joinの前は連結部分に何を入れるか''なので何もいれてない
# zipはstr1とstr2をラップする（ひとまとめとしてみる）為に書いている
# str1 = 'パトカー'
# str2 = 'タクシー'
# result = ''.join([a+b for(a, b) in zip(str1, str2)])
# # print(result)  # パタトクカシーー

# print([a+b for(a, b) in zip(str1, str2)])

# Q3
# reライブラリをインポートし、splitとreplaceで分割
# import re
# str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'


# split_after = re.split('\s', str.replace('.', '').replace(',',''))
# print(split_after)

# print([len(word) for word in split_after ])

# Q4
# あ、添字取ってくるの忘れてました！
# string = []
# string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

# print(string)

# string = string.split()

# tmp = {}

# for i, word in enumerate(string,1) :
#   if i in [1,5,6,7,8,9,15,16,19]:
#     tmp[word[0]] = i
#     print(tmp)
#   else:
#     tmp[word[0:2]] = i
#     print(tmp)

# str1 = string[0][0]
# str5 = string[4][0]
# str6 = string[5][0]
# str7 = string[6][0]
# str8 = string[7][0]
# str9 = string[8][0]
# str15 = string[14][0]
# str16 = string[15][0]
# str19 = string[18][0]

# result = str1 + str5 + str6 + str7 + str8 + str9 + str15 + str16 + str19

# print(result)

# result = list(result)

# print(result)

# 1, 5, 6, 7, 8, 9, 15, 16, 19

# Q5
# 1文字するやつと2文字ずつ分割したやつを作ってね


# 単語か文字家を判断するflg
# 分割する文字数を格納するcount
# def n_gram(flg):
#   string = "I am an NLPer"

#   # 単語の場合
#   if flg == 'word':
#     return string.split(' ')
#   else:
#     string = string.split(' ')
#     string = ''.join(string)
#     print(string)

#     return list(string[::1])

# def n_gram(string,n):
#   result = []

#   for i in  range(len(string) - n + 1):
#     result.append(string[i:i+n])

#   return result


# print('単語')
# print(n_gram('I am an NLPer'.split(), 2))

# print('文字')
# print(n_gram('I am an NLPer',3))




# 6
# def n_gram(st,n):
#   return [st[i:i+n] for i in range(len(st)-n+1)]


# X = set(n_gram("paraparaparadise",2))
# Y = set(n_gram("paragraph",2))

# # print(X)
# # print(Y)

# # 和集合
# print(X|Y);
# # 積集合
# print(X&Y);
# # 差集合
# print(X-Y);
# # 含まれているか
# print('se' in X);
# print('se' in Y);

# 7
# def temp(x,y,z):
#   print("{}時の{}は{}".format(x,y,z));

# temp(12,'気温',22.4)

# 8
# def cipher(target):
#   result = '';
#   for moji in target:
#     if moji.islower():
#       result += chr(219-ord(moji))
#     else:
#       result += moji
#   return result

# t = "helloworld"
# # 暗号化
# coded = cipher(t)
# print('暗号化:' + coded)

# # 復号化
# decoded = cipher(coded)
# print('復号化:' + decoded)

# 9
import random
# https://qiita.com/segavvy/items/be0f59af4b410069516d

string = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind'


def Typoglycemia(target):
  # リストを作る
  result = []

  # 空白区切りでリストにする
  for i in target.split(' '):
    # iに単語が入ってるので、5文字以上なら
    if len(i) >= 5:
      # 先頭の文字を格納
      tmp_first = i[0]
      # 最後尾の文字を格納
      tmp_last = i[-1]
      # 残りの順番をランダムにシャッフル
      tmp_list = i[1:-1]
      print(type(tmp_list))
      tmp_list = random.sample(tmp_list,k=len(tmp_list))

      # # 合体
      result.append(tmp_first + ''.join(tmp_list) + tmp_last)
      # print(result)
    else:
      # 3文字以下の場合は何もしないのでそのまま追加する
      result.append(i)

  # リスト型になっているresultを' 'で区切って文字列にする
  result = (' '.join(result))
  # 結果を返却する
  return result

# 文字列じゃないと表示できない？らしい
print(Typoglycemia(string))
print(Typoglycemia(string))
