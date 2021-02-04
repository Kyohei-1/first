# dic_data = [
#     {'kaku': 'は', 'kou': 'ジョン・マッカーシーは'},
#     {'kaku': 'で', 'kou': '会議で'},
#     {'kaku': 'を', 'kou': '用語を'}
# ]

def sort_kaku_kou(kaku, kou):
    kaku_data = ['は', 'で', 'を']
    kou_data = ['ジョン・マッカーシーは', '会議で', '用語を']
    dic_list = []
    # i = 1
    kaku = []
    kou = []
    for item1, item2 in zip(kaku_data, kou_data):
        dic_list.append({
            'kaku': item1,
            'kou': item2
        })
    # print(dic_list)

    sorted_data = sorted(dic_list, key=lambda x: x['kaku'])

    kaku = [chunk_dict["kaku"] for chunk_dict in sorted_data]
    kou = [chunk_dict["kou"] for chunk_dict in sorted_data]
    #
    # for data1 in sorted_data:
    #     # print(data1)
    #     for data2 in data1.values():
    #         if i % 2 == 0:
    #             kou.append(data2)
    #             i += 1
    #         else:
    #             kaku.append(data2)
    #             i += 1

    return kaku, kou
