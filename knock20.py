# coding: utf-8
import json
import gzip
import sys

filePath = sys.argv[1]
with open('./KF20.txt', 'w') as wFile:
    with gzip.open(filePath, "r") as file:
        for line in file:
            article = json.loads(line)
            if article["title"] == "イギリス":
                wFile.write(article["text"]+'\n')


# python knock20.py ./jawiki-country.json
