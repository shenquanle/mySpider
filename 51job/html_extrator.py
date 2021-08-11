from lxml import etree
import csv
import time
import random
import os
import pandas as pd
import lxml.html
import re

# 4.8备份
# def judge_num(ch):
#     if ch >= '0' and ch <= '9':
#         return True
#     else:
#         return False
#
# def count_ch(line_content):
#     num = 0
#     for i in line_content:
#         if i>='A'and i<='Z':
#             num+=1
#         if i>='a'and i<='z':
#             num += 1
#     return num
#
# def count_digit(line_content):
#     num = 0
#     for i in line_content:
#         if i >='0' and i<='9':
#             num += 1
#     return num
#
# def extractor_and_write(name):
#     num = 0
#     for file in os.listdir('./岗位2/'+name):
#         file_path = './岗位2/'+name + '/' + file
#         num += 1
#         # if num == 2:
#         #     print(file)
#         print(num)
#         print(file)
#
#         try:
#             with open(file_path, encoding='gbk') as f:
#                 content = f.read()
#                 html = lxml.html.fromstring(content)
#                 # html = etree.HTML(content)
#                 text = html.xpath("//div[@class='bmsg job_msg inbox']//p | //div[@class='bmsg job_msg inbox']//div |"
#                                   " //div[@class='bmsg job_msg inbox']//ol")
#                 # print(text)
#                 with open('./' + '岗位要求2/' + name + '/' + str(num) + '.txt', 'w', encoding='utf-8') as ff:
#                     write_judge = 0
#                     for line in text:
#                         line_content = line.xpath('string(.)')
#                         line = str(line_content).replace('\xa0', '').replace('\n', '').replace(' ','').replace('◆','').replace('?','').replace('>','').replace('×','')
#
#                         if not len(line)  or 'Summary'in line_content or '薪资'in line_content or '岗位'in line_content:
#                             continue
#                         if '微信分享' in line or '关键字' in line_content or '职能类别'in line_content or '薪酬'in line_content or '福利'in line_content or '亮点'in line_content or 'シ' in line_content:
#                             break
#                         if len(line) < 4 or line[-1] == ',' or line[-1] == '、':
#                             ff.write(line)
#                             continue
#                         if ('；' in line and line.count('；') >1) or line.count('。')>1:
#                             line_list = re.split('；|。|\?',line)
#                             for li in line_list:
#                                 ff.write(li + '\n')
#                             continue
#                         ff.write(line + '\n')
#                         # if '职位要求' in line or '岗位要求' in line or '任职要求' in line or '任职资格' in line:
#                         #     write_judge = 1
#                         #     ff.write(line + '\n')
#                         #
#                         # if write_judge == 1 and judge_num(line[0]):
#                         #     ff.write(line + '\n')
#         except Exception as e:
#             print(e)
#
# def write_together(name):
#     num = 0
#     with open('./' + '岗位要求2/'+name+'4.txt', 'a',encoding='utf-8') as ff:
#         for file in os.listdir('./' + '岗位要求2/' + name):
#             file_path = './' + '岗位要求2/' + name + '/' + file
#             # print(file_path)
#
#             with open(file_path, encoding='utf-8') as f:
#                 content = f.readlines()
#                 if len(content):
#                     num += 1
#                     print(num)
#                     print(file)
#                 for line_content in content:
#                     line_content = line_content.replace('\n', '').replace('—','').replace('\t','').replace(' ','')\
#                         .replace('－','').replace('-','').replace('*','').replace('　','').replace('?','').replace('●','').replace('<','').replace('>','')
#                     if len(line_content) <= 7 or '职能类别'in line_content or '岗位职责'in line_content or '工作时间'in line_content or '【'in line_content:
#                         continue
#                     if re.findall("1[3-9]\\d{9}", line_content) or re.findall("0\\d{2,3}-[1-9]\\d{6,7}", line_content) or 'com' in line_content:
#                         continue
#                     if 'http' in line_content or '薪' in line_content  or '地址' in line_content or count_digit(line_content)>=7 or '交通' in line_content:
#                         continue
#                     if count_ch(line_content)>20 or '休息'in line_content or '公司'in line_content or 'www' in line_content:
#                         continue
#                     if '地点' in line_content or 'Responsibility' in line_content:
#                         break
#                     if '关键字' in line_content or '加入我们' in line_content or 'xa' in line_content or '关于我们' in line_content or '单位' in line_content:
#                         break
#                     if line_content[-1] != '\n':
#                         line_content+='\n'
#                     ff.write(str(num)+'\t'+line_content)
#             # ff.write('\n')
#
# name = '游戏'
#
# extractor_and_write(name)
# write_together(name)

def judge_num(ch):
    if ch >= '0' and ch <= '9':
        return True
    else:
        return False

def count_ch(line_content):
    num = 0
    for i in line_content:
        if i>='A'and i<='Z':
            num+=1
        if i>='a'and i<='z':
            num += 1
    return num

def count_digit(line_content):
    num = 0
    for i in line_content:
        if i >='0' and i<='9':
            num += 1
    return num

def extractor_and_write(name):
    num = 0
    for file in os.listdir('./岗位2/'+name):
        file_path = './岗位2/'+name + '/' + file

        try:
            with open(file_path, encoding='gbk') as f:
                content = f.read()
                if '大数据' in content and content.count('大数据')>1:
                    num += 1
                    # if num == 2:
                    #     print(file)
                    print(num)
                    print(file)
                    # html = lxml.html.fromstring(content)
                    html = etree.HTML(content)
                    text = html.xpath("//div[@class='bmsg job_msg inbox']//p | //div[@class='bmsg job_msg inbox']//div |"
                                      " //div[@class='bmsg job_msg inbox']//ol")
                    # print(text)
                    with open('./' + '岗位要求2/' + name + '/' + str(num) + '.txt', 'w', encoding='utf-8') as ff:
                        write_judge = 0
                        for line in text:
                            line_content = line.xpath('string(.)')
                            line = str(line_content).replace('\xa0', '').replace('\n', '').replace(' ','').replace('◆','').replace('?','').replace('>','').replace('×','')

                            if not len(line)  or 'Summary'in line_content or '薪资'in line_content or '岗位'in line_content:
                                continue
                            if '微信分享' in line or '关键字' in line_content or '职能类别'in line_content or '薪酬'in line_content or '福利'in line_content or '亮点'in line_content or 'シ' in line_content:
                                break
                            if len(line) < 4 or line[-1] == ',' or line[-1] == '、':
                                ff.write(line)
                                continue
                            if ('；' in line and line.count('；') >1) or line.count('。')>1:
                                line_list = re.split('；|。|\?',line)
                                for li in line_list:
                                    ff.write(li + '\n')
                                continue
                            ff.write(line + '\n')
                            # if '职位要求' in line or '岗位要求' in line or '任职要求' in line or '任职资格' in line:
                            #     write_judge = 1
                            #     ff.write(line + '\n')
                            #
                            # if write_judge == 1 and judge_num(line[0]):
                            #     ff.write(line + '\n')
                else:
                    continue
        except Exception as e:
            print(e)

def write_together(name):
    num = 0
    with open('./' + '岗位要求2/'+name+'4.txt', 'a',encoding='utf-8') as ff:
        for file in os.listdir('./' + '岗位要求2/' + name):
            file_path = './' + '岗位要求2/' + name + '/' + file
            # print(file_path)
            with open(file_path, encoding='utf-8') as f:
                content = f.readlines()
                if len(content):
                    num += 1
                    print(num)
                    print(file)
                for line_content in content:
                    line_content = line_content.replace('\n', '').replace('—','').replace('\t','').replace(' ','')\
                        .replace('－','').replace('-','').replace('*','').replace('　','').replace('?','').replace('●','').replace('<','').replace('>','')
                    if len(line_content) <= 7 or '职能类别'in line_content or '岗位职责'in line_content or '工作时间'in line_content or '【'in line_content:
                        continue
                    if re.findall("1[3-9]\\d{9}", line_content) or re.findall("0\\d{2,3}-[1-9]\\d{6,7}", line_content) or 'com' in line_content:
                        continue
                    if 'http' in line_content or '薪' in line_content  or '地址' in line_content or count_digit(line_content)>=7 or '交通' in line_content:
                        continue
                    if count_ch(line_content)>20 or '休息'in line_content or '公司'in line_content or 'www' in line_content:
                        continue
                    if '地点' in line_content or 'Responsibility' in line_content:
                        break
                    if '关键字' in line_content or '加入我们' in line_content or 'xa' in line_content or '关于我们' in line_content or '单位' in line_content:
                        break
                    if line_content[-1] != '\n':
                        line_content+='\n'
                    ff.write(str(num)+'\t'+line_content)
            # ff.write('\n')

name = '数据'

# extractor_and_write(name)
write_together(name)