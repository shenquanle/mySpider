import jieba.analyse
import imageio
import jieba.posseg as pseg
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
import numpy as np
import csv
import collections

def jieba_cut(name):

    #停用词
    original_urls = open('./无关词.csv')
    remove_items = csv.reader(original_urls)
    remove_list = []
    for remove in remove_items:
        remove_list.append(remove[0])
    print(remove_list)  #输出停用词
    #输出文本词语出现的次数

    with open('E:/PycharmProjects/51job/岗位要求2/'+name+'.txt','r',encoding='utf-8') as f:
        s=f.read()
    words=jieba.cut(s)
    text_list = ''
    top_list = []
    for word in words:
        if (len(word) > 1 and not word in remove_list) and word:
            top_list.append(word)
            text_list = text_list + ' ' + word

    # 词频统计
    # word_counts = collections.Counter(top_list)  # 对分词做词频统计
    # word_counts_top200 = word_counts.most_common(200)  # 获取前200最高频的词来生成词云
    # print(word_counts_top200)  # 输出检查

    # # fr.close()
    # ##print(word_list)
    # print(word_dict) #输出词语出现的次数
    #
    # #按次数进行排序
    # sort_words=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
    # print(sort_words)#输出前0-100的词
    #
    #
    color_mask = np.array(Image.open("E:/PycharmProjects/51job/岗位要求/底图.jpg"))
    wc = WordCloud(
            background_color="white",  # 背景颜色
            max_words=100,  # 显示最大词数
            font_path="C:/Windows/Fonts/msyhbd.ttc",  # 使用字体
            # min_font_size=15,
            # max_font_size=50,
            height=1200,
            width=1600,
            mask=color_mask) # 图幅宽度

    wc.generate(text_list)
    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    # wc.to_file(str(i)+".png")

name = '移动开发'
jieba_cut(name)

# def jieba_cut(name):
#     #西游记停用词
#     # fr = open('西游记停用词.txt', 'r')
#     # stop_word_list = fr.readlines()
#     new_stop_word_list = []
#     # for stop_word in stop_word_list:
#     #     stop_word = stop_word.replace('\ufeef', '').strip()
#     #     new_stop_word_list.append(stop_word)
#     # print(stop_word_list)  #输出停用词
#     #输出西游记 词语出现的次数
#     s = '爸爸的儿子，妈妈的儿子，小红，小红，小红，小红，小红，小红，小红，小红，小红，小红'
#     # with open('E:/PycharmProjects/51job/岗位要求2/' + name + '.txt', 'r', encoding='utf-8') as f:
#     #     s=f.read()
#     words=jieba.cut(s)
#     word_dict={}
#     word_list=''
#     for word in words:
#         if (len(word) > 1 and not word in new_stop_word_list):
#             word_list = word_list + ' ' + word
#             if (word_dict.get(word)):
#                 word_dict[word] = word_dict[word] + 1
#             else:
#                 word_dict[word] = 1
#     ##print(word_list)
#     #print(word_dict) #输出西游记 词语出现的次数
#
#     #按次数进行排序
#     sort_words=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
#     print(sort_words[0:101])#输出前0-100的词
#
#     from wordcloud import WordCloud
#     color_mask = np.array(Image.open("E:/PycharmProjects/51job/岗位要求/底图.jpg"))
#     wc = WordCloud(
#             background_color="white",  # 背景颜色
#             max_words=3,  # 显示最大词数
#             font_path="C:/Windows/Fonts/msyhbd.ttc",  # 使用字体
#             # min_font_size=15,
#             # max_font_size=150,
#             width=400,
#             height=860,
#             mask=color_mask) # 图幅宽度
#     i=str('why')
#     print(word_list)
#     wc.generate(word_list)
#
#     plt.figure()
#     plt.imshow(wc, interpolation="bilinear")
#     plt.axis("off")
#     plt.show()
#
# name = '移动开发'
# jieba_cut(name)
