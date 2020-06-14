import json
import gzip
import sys

filePath = sys.argv[1]
# パスを取得

with gzip.open(filePath, "r") as file1:
  # gzip.openにしてるのはgzファイルを自動で解凍して、処理が終わったら圧縮してほしいから
  # 開いて読み込んだ情報がfileに入ってる
    for line in file1:
        # print(file)
        # print(line)
        # lineには1行ずつ入る感じだね
        article = json.loads(line)
        # jsonファイルの情報を辞書型で読み込む
        # print(article)
        if article["title"] == "イギリス":
          # 記事名がtitleで取れるのでイギリスに関するものを取得
            # print(article)
            print(article["text"])
            # イギリスに関する本文を取りたいので
            with open('./knock20_result.txt', 'w') as File2:
              # 書き込む準備するやで
                File2.write(article["text"])
                # 書き込むやで

                # python knock20.py ./jawiki-country.json.gz
