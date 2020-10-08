# coding: utf-8

# 40. 係り受け解析結果の読み込み（形態素）
# 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．

class Morph:
  def __init__(self,data):
    self.surface = data['surface'] #表層形
    self.surface = data['base'] #基本形
    self.pos = data['pos'] #品詞
    self.pos1 = data['pos1'] #品詞細分類1

# 行頭文字判定
def first_character_decision(data):
  global decision_candidates

  if not data.startswith(decision_candidates):
    return data

# \tで区切って表層系などに分ける
def split_t_and_parse(data):
  splitted_data = data.split('\t')
  # =====表層系=====
  surface = splitted_data[0]
  # =====表層系以外=====
  splitted_data = splitted_data[-1].split(',')
  # =====原型（基本形）=====
  base = splitted_data[6]
  # =====品詞=====
  pos = splitted_data[0]
  # =====品詞細分類=====
  pos1 = splitted_data[1]

  parsed_data= {
    'surface':surface,
    'base':base,
    'pos':pos,
    'pos1':pos1
  }


  return parsed_data


# 行頭文字判定タプル
decision_candidates = ('*',"'",'n')
document = [] #文全体を入れるリスト
sentence = [] #EOS区切りの異聞を入れるリスト

#ファイルのパスを格納
path = './data/ai.ja.txt.parsed'
# 読み込みでファイルを開いとく
with open(path, 'r') as read_data:
  for read_text in read_data:
    data = first_character_decision(read_text)
    if data is not None: # 行頭がEOSでないなら
      data = split_t_and_parse
      print(data)
    else: #行頭がEOSならそこまでを一文とする
      print('草')
