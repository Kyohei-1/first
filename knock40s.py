# # coding: utf-8
# import re

# with open('./ai.ja.txt') as read_file:
#   read_text = read_file.readlines()
#   read_text.split('。',read_text)
#   print(read_text)


# with open('./parse.txt', 'w') as write_file:
#     with open('./ai.ja.txt', 'r') as read_file:
#         for text in readFile:
#             listData = text.split('。')
#             for data in listData:
#               print(''.join(str(data)))

path = './ai.ja.txt'

with open('./out/ai.parse.txt', 'w') as writeFile:
    with open(path, 'r') as readFile:
        for text in readFile:
            text = text.split('。')
            print(text)
