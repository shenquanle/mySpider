# -*- coding: utf-8 -*-
import csv
import time
import os
import re
import random

from selenium import webdriver
from lxml import etree
import urllib.request
from fake_useragent import UserAgent
import pandas as pd



def create_dir(name, dir_list):
    base_path = "./" + name + "/"

    created_dir_list = []

    for dir_name in dir_list:
        created_dir_list.append(base_path + dir_name)
        if not os.path.exists(base_path + dir_name):
            os.mkdir(base_path + dir_name)
            print("创建文件夹成功")
        else:
            print("文件夹已存在")

    return created_dir_list

def write_href_to_csv(dir_path, target_url_list):
    with open(dir_path + '/href_list.csv', 'w', encoding='utf-8', newline='') as csv_file:
        # 获取一个csv对象进行写入
        writer = csv.writer(csv_file)
        for url in target_url_list:
            if '腾讯' in dir_path and url[0] == '/':
                url = "https://news.qq.com" + url
            if '新浪' in dir_path and url[0] == '/':
                url = "http://news.sina.com.cn" + url
            if '搜狐' in dir_path and url[0] == '/':
                url = "http://news.sohu.com" + url
            if '中国天气' in dir_path and url[0] == '/':
                url = "http://www.weather.com.cn" + url

            # writerow 写入一行数据
            url_list =[]
            url_list.append(url)
            writer.writerow(url_list)
    print("href写入文件成功")

def get_target_url(dir_name, gov_url):
    option = webdriver.ChromeOptions()
    # prefs = {"profile.managed_default_content_settings.images": 2}
    # option.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=option,executable_path=r'./chromedriver.exe')
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(5)
    try:
        driver.get(gov_url)
    except Exception:
        driver.execute_script('window.stop()')
    time.sleep(4)
    """"
    输入应急预案，并完成搜索
    """
    html_content = driver.page_source
    html = etree.HTML(html_content)
    # 先尝试偏门的规则，若提取不到再重新赋值，再提取

    target_url_list = []

    if '腾讯' in dir_name:
        # 提取当前页的url
        page_num = 1

        url_rule = "//td[@class='lh_26 font14px']/a/@href"
        url_list = html.xpath(url_rule)
        if not len(url_list):
            url_rule = "//div[@class='leftList']//a[@target='_blank']/@href"
            url_list = html.xpath(url_rule)
        if not len(url_list):
            url_rule = "//div[@class='layout-content-left']//h4[@class='title']/a/@href"
            url_list = html.xpath(url_rule)

        target_url_list.extend(url_list)

        # 判断下一页按钮是否存在
        next_page_rule = "//a[text()='下一页>']"
        next_page = html.xpath(next_page_rule)

        print("下一页存在状态：", len(next_page))
        time.sleep(5)
        while len(next_page):
            try:
                element = driver.find_element_by_xpath(next_page_rule)
                driver.execute_script("arguments[0].click();", element)
                time.sleep(3)
                page_num += 1
                print(next_page_rule)
                driver.switch_to.window(driver.window_handles[-1])

                print("正在爬第", page_num, "页")
                html_content = driver.page_source
                html = etree.HTML(html_content)
                # 进行目标url的提取
                url_rule = "//td[@class='lh_26 font14px']/a/@href"
                url_list = html.xpath(url_rule)
                if not len(url_list):
                    url_rule = "//div[@class='leftList']//a[@target='_blank']/@href"
                    url_list = html.xpath(url_rule)
                if not len(url_list):
                    url_rule = "//div[@class='layout-content-left']//h4[@class='title']/a/@href"
                    url_list = html.xpath(url_rule)

                target_url_list.extend(url_list)

                time.sleep(random.randint(2, 6))
                if page_num == 20:
                    break
                html_content = driver.page_source
                html = etree.HTML(html_content)
                next_page = html.xpath(next_page_rule)
            except Exception as e:
                print(e)
                break
        time.sleep(5)
        driver.quit()
        return target_url_list

    if '新浪' in dir_name:
        # 提取当前页的url
        page_num = 1

        url_rule = "//span[@class='title14']//li/a/@href"
        url_list = html.xpath(url_rule)
        if not len(url_list):
            url_rule = "//span[@class='c_tit']/a/@href"
            url_list = html.xpath(url_rule)
        if not len(url_list):
            url_rule = "//div[@class='layout-content-left']//h4[@class='title']/a/@href"
            url_list = html.xpath(url_rule)

        target_url_list.extend(url_list)

        # 判断下一页按钮是否存在
        next_page_rule = "//a[text()='下一页']"
        next_page = html.xpath(next_page_rule)

        print("下一页存在状态：", len(next_page))
        time.sleep(5)
        while len(next_page):
            try:
                element = driver.find_element_by_xpath(next_page_rule)
                driver.execute_script("arguments[0].click();", element)
                time.sleep(3)
                page_num += 1
                print(next_page_rule)
                driver.switch_to.window(driver.window_handles[-1])

                print("正在爬第", page_num, "页")
                html_content = driver.page_source
                html = etree.HTML(html_content)
                # 进行目标url的提取
                url_rule = "//span[@class='title14']//li/a/@href"
                url_list = html.xpath(url_rule)
                if not len(url_list):
                    url_rule = "//span[@class='c_tit']/a/@href"
                    url_list = html.xpath(url_rule)
                if not len(url_list):
                    url_rule = "//div[@class='layout-content-left']//h4[@class='title']/a/@href"
                    url_list = html.xpath(url_rule)

                target_url_list.extend(url_list)

                time.sleep(random.randint(2, 6))
                if page_num == 20:
                    break
                html_content = driver.page_source
                html = etree.HTML(html_content)
                next_page = html.xpath(next_page_rule)
            except Exception as e:
                print(e)
                break
        time.sleep(5)
        driver.quit()
        return target_url_list

    if '搜狐' in dir_name:
        # 提取当前页的url
        page_num = 1

        url_rule = "/li/a/@href"
        url_list = html.xpath(url_rule)
        if not len(url_list):
            url_rule = "//div[@class='f14list']//li/a/@href"
            url_list = html.xpath(url_rule)
        if not len(url_list):
            url_rule = "//td[@class='line_space']//li/a/@href"
            url_list = html.xpath(url_rule)
        if not len(url_list):
            url_rule = "//a[@class='newsblue1']/@href"
            url_list = html.xpath(url_rule)
        if not len(url_list):
            url_rule = "//div[@class='block10']//a/@href"
            url_list = html.xpath(url_rule)
        print("有",len(url_list),"条链接")
        target_url_list.extend(url_list)

        # 判断下一页按钮是否存在
        next_page_rule = "//a[text()='下一页']"
        next_page = html.xpath(next_page_rule)

        print("下一页存在状态：", len(next_page))
        time.sleep(5)
        while len(next_page):
            try:
                element = driver.find_element_by_xpath(next_page_rule)
                driver.execute_script("arguments[0].click();", element)
                time.sleep(3)
                page_num += 1
                print(next_page_rule)
                driver.switch_to.window(driver.window_handles[-1])

                print("正在爬第", page_num, "页")
                html_content = driver.page_source
                html = etree.HTML(html_content)
                # 进行目标url的提取
                url_rule = "/li/a/@href"
                url_list = html.xpath(url_rule)
                if not len(url_list):
                    url_rule = "//div[@class='f14list']//li/a/@href"
                    url_list = html.xpath(url_rule)

                target_url_list.extend(url_list)

                time.sleep(random.randint(2, 6))
                if page_num == 30:
                    break
                html_content = driver.page_source
                html = etree.HTML(html_content)
                next_page = html.xpath(next_page_rule)
            except Exception as e:
                print(e)
                break
        time.sleep(5)
        driver.quit()
        return target_url_list

    if '中国天气' in dir_name:
        # 提取当前页的url
        page_num = 1

        url_rule = "//div[@class='l']//a/@href"
        url_list = html.xpath(url_rule)
        if not len(url_list):
            url_rule = "//div[@class='content_list1']//a/@href"
            url_list = html.xpath(url_rule)
        if not len(url_list):
            url_rule = "//div[@class='zb']//h3/a/@href"
            url_list = html.xpath(url_rule)


        target_url_list.extend(url_list)

        driver.quit()
        return target_url_list

    if '气象局' in dir_name:
        # 提取当前页的url
        page_num = 1

        url_rule = "//div[@class='con_list_news_zt']/a/@href"
        url_list = html.xpath(url_rule)


        target_url_list.extend(url_list)

        # 判断下一页按钮是否存在
        next_page_rule = "//a[text()='下一页']"
        next_page = html.xpath(next_page_rule)

        print("下一页存在状态：", len(next_page))
        time.sleep(5)
        while len(next_page):
            try:
                element = driver.find_element_by_xpath(next_page_rule)
                driver.execute_script("arguments[0].click();", element)
                time.sleep(3)
                page_num += 1
                print(next_page_rule)
                driver.switch_to.window(driver.window_handles[-1])

                print("正在爬第", page_num, "页")
                html_content = driver.page_source
                html = etree.HTML(html_content)
                # 进行目标url的提取
                url_rule = "//div[@class='con_list_news_zt']/a/@href"
                url_list = html.xpath(url_rule)

                target_url_list.extend(url_list)

                time.sleep(random.randint(2, 6))
                if page_num == 30:
                    break
                html_content = driver.page_source
                html = etree.HTML(html_content)
                next_page = html.xpath(next_page_rule)
            except Exception as e:
                print(e)
                break
        time.sleep(5)
        driver.quit()
        return target_url_list


def get_target_data(dir_path, href, run_time):

    # 必须进行异常的处理，防止有些代理和ua不好使，从而防止程序终止
    try:
        # 每8个网址就换一次好使的代理和对应ua
        user_agent = UserAgent().random
        print("当前网页链接为：" + href)
        header = {'User-Agent':  user_agent}
        req = urllib.request.Request(href, headers=header)
        try:
            html_content = urllib.request.urlopen(req).read().decode('utf-8')
        except Exception:
            html_content = urllib.request.urlopen(req).read().decode('gbk', 'ignore')

        html = etree.HTML(html_content)

        # 由于txt文件的命名不能出现 / :* ?“ < > ”等特殊符号，所以必须替换掉/
        # 由于网页中有Unicode特殊编码，必须encoding一下才能写进默认编码为gbk的txt文件
        if "腾讯" in dir_path:
            title_rule = "//div[@class='hd']/h1/text()"
            source_rule = "//span[@class='color-a-1' or @class='where']/a/text()"
            source = html.xpath(source_rule)
            if not len(source):
                source_rule = "//span[@class='where']/text()"
            time_rule = "//span[@class='article-time' or @class='pubTime']/text()"
            time = html.xpath(time_rule)
            if not len(time):
                time_rule = "//div[@class='info']/text()"
            paragraph_rule = "//div[@id='Cnt-Main-Article-QQ']//p/text()"
        if "新浪" in dir_path:
            title_rule = "//th[@class='f24']/font/text()"
            title = html.xpath(title_rule)
            if not len(title):
                title_rule = "//h1[@id='artibodyTitle']/text()"
            if not len(title):
                title_rule = "//h1/text()"
            source_rule = "//td[@height='20']/font/text()"
            source = html.xpath(source_rule)
            if not len(source):
                source_rule = "//span[@data-sudaclick='media_name' or @id='media_name']/a/text()"
            time_rule = "//td[@height='20']/text()"
            time = html.xpath(time_rule)
            if not len(time):
                time_rule = "//span[@id='pub_date']/text()"
            paragraph_rule = "//td[@class='l17']/p/text()"
            paragraph = html.xpath(paragraph_rule)
            if not len(paragraph):
                paragraph_rule = "//div[@class='blkContainerSblk' or @id='artibody']//p/text()"
            if not len(paragraph):
                paragraph_rule = "//font[@id='zoom']/p/text()"
        if "搜狐" in dir_path:
            title_rule = "//div[@class='content-box clear']/h1/text()"
            title = html.xpath(title_rule)
            if not len(title):
                title_rule = "//td[@align='center']/font/b/text()"
            source_rule = "//span[@id='media_span']/a/text()"
            source = html.xpath(source_rule)
            if not len(source):
                source_rule = "//td[@align='center']/text()"
            time_rule = "//div[@class='time']/text()"
            time = html.xpath(time_rule)
            if not len(time):
                time_rule = "//td[@align='center']/text()"
            paragraph_rule = "//div[@id='contentText']/text()"
            paragraph = html.xpath(paragraph_rule)
            if not  len(paragraph):
                paragraph_rule = "//td[@class='line_space2']//p/text()"
        if "中国天气" in dir_path:
            title_rule = "//p[@class='articleTittle']/text()"
            source_rule = "//div[@class='articleTimeSizeleft']/span[2]/a/text()"
            time_rule = "//div[@class='articleTimeSizeleft']/span[1]/text()"
            paragraph_rule = "//div[@class='articleBody']//p/text()"
            paragraph = html.xpath(paragraph_rule)
            if not len(paragraph):
                paragraph_rule = "//div[@class='articleBody']//text()"
        print(paragraph_rule)
        title = html.xpath(title_rule)
        source = html.xpath(source_rule)
        time = html.xpath(time_rule)
        paragraph = html.xpath(paragraph_rule)

        if not len(title) and not len(source) and not len(time) and not len(paragraph):
            raise TypeError("腾讯跳转错误")


        # print(type(title))
        print(title)
        # print(type(source))
        print(source)
        # print(type(time))
        print(time)
        # print(type(paragraph))
        print(paragraph)


        title_name = title[0].replace('\n','').replace('\t','').replace('\n\t','').replace('\u3000','').replace('\r','').replace(' ','')
        title_name = re.sub('[\/:*?"<>|]', '-', title_name)
        print(title_name)
        with open(dir_path + '/' + title_name + '.txt', 'w', encoding='utf-8-sig', newline='') as f:
            f.write(title_name+'\n')
            if '\u3000' in source[0]:
                f.write(source[0].split('\u3000')[1]+'\n')
            else:
                f.write(source[0] + '\n')

            if '\u3000' in time[0]:
                f.write(time[0].split('\u3000')[0]+'\n')
            else:
                f.write(time[0] + '\n')
            for line in paragraph:
                f.write(line.replace('\r','').replace('\n','').replace('\u3000','')+'\n\n')
        print("存储成功")
        f.close()
        print("正在爬第" + str(run_time) + "个网页数据")
    except Exception as e:
        print(e)
        raise TypeError("访问失败")

if __name__ == '__main__':

    excel_file_path = "./需要爬取.xlsx"
    data = pd.read_excel(excel_file_path, sheet_name=['腾讯','新浪','搜狐','中国天气','气象局'])

    tencent_name_list = data['腾讯']['台风']
    tencent_url_list = data['腾讯']['链接']

    sina_name_list = data['新浪']['台风']
    sina_url_list = data['新浪']['链接']

    sohu_name_list = data['搜狐']['台风']
    sohu_url_list = data['搜狐']['链接']

    chn_name_list = data['中国天气']['台风']
    chn_url_list = data['中国天气']['链接']

    weather_name_list = data['气象局']['台风']
    weather_url_list = data['气象局']['链接']

    tencent_dir_list = create_dir('腾讯', tencent_name_list)
    sina_dir_list = create_dir('新浪', sina_name_list)
    sohu_dir_list = create_dir('搜狐', sohu_name_list)
    chn_dir_list = create_dir('中国天气', chn_name_list)
    weather_dir_list = create_dir('气象局', weather_name_list)

    # 获取每个台风链接下的所有url列表，并存入csv文件中
    # for dir, url in zip(sohu_dir_list, sohu_url_list):
    #     if url == 0 or url == '0':
    #         continue
    #     else:
    #         print(dir, url)
    #         target_url_list = get_target_url(dir, url)
    #         write_href_to_csv(dir, target_url_list)
    #         time.sleep(random.randint(4,8))


    for dir_list in [tencent_dir_list, sina_dir_list, sohu_dir_list, chn_dir_list]:
    # for dir_list in [sina_dir_list]:
    #     dir_list = ['./新浪/新浪-2005-海棠台风']
        for dir_path in dir_list:
            print(dir_path)
            try:
                typhoon_csv = open(dir_path+'\href_list.csv')
                typhoon_csv_items = csv.reader(typhoon_csv)
                target_url_list = [href[0] for href in typhoon_csv_items]
                run_time = 0

                print(target_url_list)
                for target_url in target_url_list:
                    print(target_url)
                    try:
                        get_target_data(dir_path, target_url, run_time)
                        run_time += 1
                        time.sleep(random.randint(3, 6))
                    except Exception as e:
                        print(e)
                        continue
            except Exception as e:
                print(e)
                continue