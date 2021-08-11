# import requests
# from lxml import etree
# import csv
# import time
# import random
#
# import pandas as pd
# from requests.adapters import HTTPAdapter

#
# s = requests.Session()
# s.mount('http://', HTTPAdapter(max_retries=3))
# s.mount('https://', HTTPAdapter(max_retries=3))
# e_list = []
# for i in range(1,2001):
#     if i % 8 == 1:
#         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
#     elif i % 8 == 4:
#         headers = {"User-Agent": "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"}
#     elif i % 8 == 7:
#         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
#     else:
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
#     url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE,2,'+str(i)+'.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
#
#     requests_get = s.get(url, headers=headers, timeout=10)
#     print('第'+str(i)+'个','状态码:'+ str(requests_get.status_code))
#     requests_get.encoding = "gbk"
#
#     # print(requests_get.content.decode('gbk'))
#     # with open('./test.txt','utf-8') as f:
#     #     content = f.read()
#     html = etree.HTML(requests_get.content)
#     url_list = html.xpath("//div[@class='el']/p//a/@href")
#
#     if len(url_list) != 50:
#         e_list.append(i)
#     # print(url_list)
#     print(len(url_list))
#     # 字典中的key值即为csv中列名
#     dataframe = pd.DataFrame(url_list)
#
#     # 将DataFrame存储为csv,index表示是否显示行名，default=True
#     # dataframe.to_csv("test.csv",index=None,sep=',')
#     dataframe.to_csv('数据.csv', index=None, mode='a')
#
#     time.sleep(random.randint(3,8))
# # print(len(target_url_list))
# # # print(target_url_list)
# # target_url_list = ['https://jobs.51job.com/shenzhen-ftq/120441224.html?s=01&t=0', 'https://jobs.51job.com/shenzhen-ftq/119340599.html?s=01&t=0', 'https://jobs.51job.com/wuhan/120449667.html?s=01&t=0', 'https://jobs.51job.com/shenzhen/120669471.html?s=01&t=0', 'https://jobs.51job.com/shenzhen/120840522.html?s=01&t=0', 'https://jobs.51job.com/shanghai/120166833.html?s=01&t=0', 'https://jobs.51job.com/nanjing/116398169.html?s=01&t=0', 'https://jobs.51job.com/suzhou/82117914.html?s=01&t=0', 'https://jobs.51job.com/shenzhen-gmxq/112496259.html?s=01&t=0', 'https://jobs.51job.com/shanghai-mhq/117068668.html?s=01&t=0', 'https://jobs.51job.com/guangzhou-hpq/120058367.html?s=01&t=0', 'https://jobs.51job.com/guangzhou-thq/115237160.html?s=01&t=0', 'https://jobs.51job.com/wuhan-hsq/121146267.html?s=01&t=0', 'https://jobs.51job.com/dalian-gxyq/121144091.html?s=01&t=0', 'https://jobs.51job.com/beijing-dcq/121143064.html?s=01&t=0', 'https://jobs.51job.com/suzhou-gxq/121137210.html?s=01&t=0', 'https://jobs.51job.com/dalian-gxyq/121134981.html?s=01&t=0', 'https://jobs.51job.com/yichang/121131247.html?s=01&t=0', 'https://jobs.51job.com/chengdu-slq/121129829.html?s=01&t=0', 'https://jobs.51job.com/guangzhou-thq/121127660.html?s=01&t=0', 'https://jobs.51job.com/shenzhen/120869101.html?s=01&t=0', 'https://jobs.51job.com/shenzhen/120865018.html?s=01&t=0', 'https://jobs.51job.com/guangzhou-byq/120014603.html?s=01&t=0', 'https://jobs.51job.com/shanghai-pdxq/119941726.html?s=01&t=0', 'https://jobs.51job.com/beijing/119305842.html?s=01&t=0', 'https://jobs.51job.com/guangzhou-nsq/119296921.html?s=01&t=0', 'https://jobs.51job.com/shanghai-pdxq/114210152.html?s=01&t=0', 'https://jobs.51job.com/guangzhou/113612569.html?s=01&t=0', 'https://jobs.51job.com/beijing/121119059.html?s=01&t=0', 'https://jobs.51job.com/beijing-hdq/121096608.html?s=01&t=0', 'https://jobs.51job.com/shanghai-ptq/104086154.html?s=01&t=0', 'https://jobs.51job.com/guangzhou-thq/101815164.html?s=01&t=0', 'https://jobs.51job.com/qingdao-sbq/119964053.html?s=01&t=0', 'https://jobs.51job.com/shanghai-ptq/117626304.html?s=01&t=0', 'https://jobs.51job.com/shenzhen-baq/120253861.html?s=01&t=0', 'https://jobs.51job.com/nanjing-qhq/115402983.html?s=01&t=0', 'https://jobs.51job.com/ningbo-yzq/120074764.html?s=01&t=0', 'https://jobs.51job.com/nanjing-qhq/121109280.html?s=01&t=0', 'https://jobs.51job.com/shenyang-hnq/121104636.html?s=01&t=0', 'https://jobs.51job.com/guangzhou-thq/121102722.html?s=01&t=0', 'https://jobs.51job.com/nanjing-glq/121095516.html?s=01&t=0', 'https://jobs.51job.com/wuxi-hsq/121093846.html?s=01&t=0', 'https://jobs.51job.com/guanchenghuizuqu/121059922.html?s=01&t=0', 'https://jobs.51job.com/dongguan-caz/120875479.html?s=01&t=0', 'https://jobs.51job.com/guangzhou-thq/120831038.html?s=01&t=0', 'https://jobs.51job.com/shenzhen/120743915.html?s=01&t=0', 'https://jobs.51job.com/beijing/120728419.html?s=01&t=0', 'https://jobs.51job.com/shenzhen/120727834.html?s=01&t=0', 'https://jobs.51job.com/guangzhou/120702727.html?s=01&t=0', 'https://jobs.51job.com/shanghai/120567990.html?s=01&t=0']
# print(e_list)
import requests
from lxml import etree
import csv
import time
import random

import pandas as pd
from requests.adapters import HTTPAdapter


s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))
e_list = []
with open('游戏.csv','w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for i in range(1,202):
        if i % 8 == 1:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
        elif i % 8 == 4:
            headers = {"User-Agent": "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"}
        elif i % 8 == 7:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        else:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE,2,'+str(i)+'.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        url = 'https://search.51job.com/list/000000,000000,7500,00,9,99,%2B,2,'+str(i)+'.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        # print(url)
        requests_get = s.get(url, headers=headers, timeout=10)
        print('第'+str(i)+'个','状态码:'+ str(requests_get.status_code))
        requests_get.encoding = "gbk"

        html = etree.HTML(requests_get.content)
        url_list = html.xpath("//div[@class='el']/p//a/@href")

        if len(url_list) != 50:
            e_list.append(i)
        print(len(url_list))
        for target_url in url_list:
            writer.writerow([target_url])

        time.sleep(random.randint(2,4))
    # print(e_list)
