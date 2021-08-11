import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import collections
from wordcloud import WordCloud, ImageColorGenerator,STOPWORDS
import jieba
import csv
import os, json
import thulac
import jiagu
from snownlp import SnowNLP
import pkuseg
import math

class WORDTest(object):
    def __init__(self, png_name, text_name):
        self.png_path = os.path.join('E:/PycharmProjects/51job/岗位要求/', png_name)
        self.text_path = os.path.join('E:/PycharmProjects/51job/岗位要求2/', text_name)
        self.pun = ['，', '。', '！', '？', '：', '、', '；', '“', '”', ' ']
        self.cloud_mask = np.array(Image.open(self.png_path))

    def open_file(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            all_data = f.read().replace('\n', '').replace(' ', '').replace('\t','').replace('*','')
        return all_data

    def write_to_png_by_text(self, data):
        wc = WordCloud(
            background_color="white",  # 背景颜色
            max_words=300,  # 显示最大词数
            font_path="C:/Windows/Fonts/msyhbd.ttc",  # 使用中文字体包STHUPO.TTF,FZSTK.TTF
            scale=28,
            # stopwords=STOPWORDS.add("数据"),  # 屏蔽词，屏蔽掉“数据”这个词
            mask=self.cloud_mask,
            # min_font_size=15,
            max_font_size=50,
            # height=600,
            # width=400  # 图幅宽度
        ).generate(data)
        # wc.to_file('test_word.png')

        plt.figure()
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.show()
    def write_to_png_by_frequancy(self, word_counts):
        wc = WordCloud(
            background_color="white",  # 背景颜色
            max_words=200,  # 显示最大词数
            font_path="C:/Windows/Fonts/msyhbd.ttc",  # 使用中文字体包STHUPO.TTF,FZSTK.TTF
            scale=28,
            # stopwords=STOPWORDS.add("数据"),  # 屏蔽词，屏蔽掉“数据”这个词
            mask=self.cloud_mask,
            # min_font_size=10,
            # max_font_size=100,
            height=1200,
            width=1600  # 图幅宽度
        )
        wc.generate_from_frequencies(word_counts)
        wc.to_file('./词云/游戏.png')

        # plt.figure()
        # plt.imshow(wc, interpolation="bilinear")
        # plt.axis("off")
        # plt.show()

    def main(self):
        mytext_list = list()
        # text = self.open_file(path=self.text_path)
        text = self.open_file(path=self.text_path)
        # jieba
        text = jieba.cut(text)

        # jiagu
        # text = jiagu.seg(text)

        # snownlp
        # text = SnowNLP(text).words

        # pkuseg
        # pku_seg = pkuseg.pkuseg()
        # text = pku_seg.cut(text)

        original_urls = open('./无关词.csv')
        remove_items = csv.reader(original_urls)
        remove_list = []
        for remove in remove_items:
            remove_list.append(remove[0])
        self.pun.extend(remove_list)

        for data in text:
            # print(data)
            if data not in self.pun and len(data) > 1 and data:
                mytext_list.append(data)
        # print(" ".join(mytext_list))

        # 词频统计
        word_counts = collections.Counter(mytext_list)  # 对分词做词频统计
        word_counts_top200 = word_counts.most_common(200)  # 获取前10最高频的词
        print(word_counts_top200)  # 输出检查

        # original_urls = open('./无关词.csv')
        # remove_items = csv.reader(original_urls)
        # remove_list = []
        # for remove in remove_items:
        #     remove_list.append(remove[0])

        # remove_list = ['开发', '技术', '相关', '良好', '优先', '产品', '以上', '完成', '优化', '平台', '需求', '沟通', '以上学历',
        #                '具有', '系统', '代码', '编程', '具备', '进行', '分析', '使用', '专业', '性能', '框架', '文档', '移动',
        #                '精通', '参与', '维护', '编写', '了解', '学习', '根据', '熟练', '测试', '软件', 'APP', '客户端', '问题',
        #                '能够', '实现', '常用', '功能', '以及', '解决', '精神', '语言', '一定', '任务', '习惯', '掌握', '各种', '内存',
        #                '质量', '原理', '要求', '配合', '程序', '研究', '较强', '业务', '工具', '至少', '微信', '过程', '方案', '考虑',
        #                '善于', '其他', '改进', '持续', '深入', '实际', '压力', '上线', '快速', '优秀', '承担', '强烈',
        #                '完整', '计划', '处理', '提升', '高质量', '核心', '保证', '基本', '协助', '基于', '环境', '自定义', '开发工具',
        #                '按照', '提供', '包括', '或者', '制定', '第三方', '方面', '丰富', '行业', '结构', '专业本科', '特性', '常见', '协调',
        #                '清晰', '思想', '客户', '迭代']
        true_words_list = []
        for word in word_counts_top200:
            if word[0] not in remove_list:
                true_words_list.append(word[0])
        true_words_dict = dict()
        for key,vaule in word_counts.items():
            if key in true_words_list:
                true_words_dict[key] = math.log(vaule,10)
                # true_words_dict[key] = vaule ** 0.125
        print(len(true_words_dict))
        # print(true_words_dict)
        print(sorted(true_words_dict.items(), key=lambda kv: (kv[1], kv[0])))
        # new_a = {}
        # for i, (k, v) in enumerate(word_counts.items()):
        #     new_a[k] = v
        #     if i == 100:
        #         print(new_a)
        #         break

        # self.write_to_png_by_frequancy(word_counts)
        self.write_to_png_by_frequancy(true_words_dict)

        # 文本生成
        # self.write_to_png_by_text(",".join(mytext_list[0:300]))


        # print(self.cloud_mask)


if __name__ == "__main__":
    png_name = '底图.jpg'
    name = '游戏'
    text_name =  name + '.txt'
    w = WORDTest(png_name=png_name, text_name=text_name)
    w.main()
"""
['开发', '技术', '相关', '良好', '优先', '产品', '以上', '完成', '优化', '平台', '需求', '以上学历',
               '具有', '系统', '代码', '编程', '具备', '进行', '分析', '使用', '专业', 
               '', '参与', '维护', '编写', '了解', '学习', '根据', '', '测试', '软件', '', '', '问题',
               '能够', '实现', '常用', '功能', '以及', '解决', '精神', '语言', '一定', '任务', '习惯', '掌握', '各种', '',
               '质量', '', '要求', '配合', '程序', '', '较强', '业务', '工具', '至少', '', '过程', '', '考虑',
               '善于', '其他', '改进', '持续', '深入', '实际', '', '上线', '快速', '优秀', '承担', '强烈',
               '完整', '计划', '处理', '提升', '', '核心', '保证', '基本', '协助', '基于', '环境', '自定义', '',
               '按照', '提供', '包括', '或者', '制定', '', '方面', '丰富', '行业', '结构', '专业本科', '特性', '常见', '',
               '清晰', '思想', '客户', '']
"""