# -*- coding: utf-8 -*-
# 実行する際はpython3で実行してね

# Q0
# str = 'stressed'
# str = str[::-1]
# print str

# Q1
# str = '「パタトクカシーー」'
# print(str[1]+str[3]+str[5]+str[7])

# Q2
# .joinの前は連結部分に何を入れるか''なので何もいれてない
# zipはstr1とstr2をラップする（ひとまとめとしてみる）為に書いている
# str1 = 'パトカー'
# str2 = 'タクシー'
# result = ''.join([a+b for(a, b) in zip(str1, str2)])
# print(result)  # パタトクカシーー

# Q3
# reライブラリをインポートし、splitとreplaceで分割
# import re
# str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

# split_after = re.split('\s', str.replace('.', ''))
# print(split_after)
# print('\n')

# Q4
# str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

# str = str.split()

# str1 = str[0][0]
# str5 = str[4][0]
# str6 = str[5][0]
# str7 = str[6][0]
# str8 = str[7][0]
# str9 = str[8][0]
# str15 = str[14][0]
# str16 = str[15][0]
# str19 = str[18][0]

# result = '' + str1 + str5 + str6 + str7 + str8 + str9 + str15 + str16 + str19;

# print(result);

# 1, 5, 6, 7, 8, 9, 15, 16, 19

# Q5
# 1文字ずつ分割するやつと2文字ずつ分割したやつを作ってね

def n_gram(str, ):
  str = str.split(' ')
  return str


str = 'I am an NLPer'

print('単語(bi-gram)'+n_gram(str,1))

print('文字(bi-gram)'+n_gram(str,2))
