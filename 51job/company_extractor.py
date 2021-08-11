from lxml import etree
import csv
import time
import random
import os
import pandas as pd
import lxml.html
import re

def extractor_and_write(name):
    num = 0
    c_name_list = []
    # for file in os.listdir('./岗位2/'+name):
    #     file_path = './岗位2/'+ name + '/' + file
    #
    #     try:
    #         with open(file_path, encoding='gbk') as f:
    #             content = f.read()
    #             if '大数据' in content and content.count('大数据') > 1:
    #                 num += 1
    #                 print(num)
    #                 print(file)
    #                 # html = lxml.html.fromstring(content)
    #                 html = etree.HTML(content)
    #                 c_name = html.xpath("//p[@class='cname']/a/@title")
    #                 c_name_list.append(c_name[0])
    #             else:
    #                 continue
    #     except Exception as e:
    #         print(e)
    # cname_list = list(set(c_name_list))
    ID = 0
    with open('./' + '岗位要求2/' + name + '/' + 'company2.txt', 'w', encoding='utf-8') as ff:
        with open('./' + '岗位要求2/' + name + '/' + 'company.txt', encoding='utf-8') as f:
            cname_list = f.readlines()
            cname_list = list(set(cname_list))
            print(cname_list)
            for cname in cname_list:
                ID+=1
                ff.write(str(ID) + '\t' + cname + '\n')

name = '后端开发'
extractor_and_write(name)

# with open('无关词.csv','w') as f:
#     writer = csv.writer(f, lineterminator='\n')
#     url_list = ['开发', '技术', '相关', '良好', '优先', '产品', '以上', '完成', '优化', '平台', '需求', '以上学历',
#                '具有', '系统', '代码', '编程', '具备', '进行', '分析', '使用', '专业',
#                '参与', '维护', '编写', '了解', '学习', '根据',  '测试', '软件','问题',
#                '能够', '实现', '常用', '功能', '以及', '解决', '精神', '语言', '一定', '任务', '习惯', '掌握', '各种',
#                '质量', '要求', '配合', '程序',  '较强', '业务', '工具', '至少',  '过程',  '考虑',
#                '善于', '其他', '改进', '持续', '深入', '实际', '上线', '快速', '优秀', '承担', '强烈',
#                '完整', '计划', '处理', '提升',  '核心', '保证', '基本', '协助', '基于', '环境', '自定义',
#                '按照', '提供', '包括', '或者', '制定', '方面', '丰富', '行业', '结构', '专业本科', '特性', '常见',
#                '清晰', '思想', '客户']
#     for target_url in url_list:
#         writer.writerow([target_url])
# original_urls = open('./无关词.csv')
# url_items = csv.reader(original_urls)
# for url in url_items:
#     print(url[0])