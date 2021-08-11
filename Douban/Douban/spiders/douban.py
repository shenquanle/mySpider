# -*- coding: utf-8 -*-
import scrapy
import string
import random
from random import choice
import json
import time
import xlrd
from selenium import webdriver
from scrapy.http.request import Request
from Douban.items import DoubanItem



class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    num = 24773958
    url = "https://movie.douban.com/subject/" + str(num) + "/comments"
    start_urls = [url + '?status=P', url + '?status=F']
    # url2 = "https://movie.douban.com/subject/5942150/comments"
    # 短评包括两种分类，P是看过，F是想看
    # start_urls = [
    #     "https://movie.douban.com/subject/5942150/comments?status=P",
    #     "https://movie.douban.com/subject/5942150/comments?status=F"
    # ]

    # start_urls = []
    # workbook = xlrd.open_workbook(r'C:\Users\shenlele\Desktop\MoviesData.xlsx')
    # sheet1 = workbook.sheet_by_name('MoviesData')
    # # 获取第3列内容，豆瓣电影ID
    # id_cols = sheet1.col_values(2)
    # for movie_id in id_cols:
    #     # 跳过第一行的标题
    #     if movie_id == 'MovieID':
    #         continue
    #     else:
    #         num = int(movie_id)
    #         url = "https://movie.douban.com/subject/" + str(num) + "/comments"
    #         start_urls.append(url + '?status=P')
    #         start_urls.append(url + '?status=F')

    # print('====================================')
    # print(start_urls)
    # print('====================================')
    # 请求头部需要携带的信息，尽可能的伪装成浏览器来访问豆瓣电影网页
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "movie.douban.com",
        "Referer": "https://movie.douban.com/",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"
    }
    '''
    cookies = {"ll": "118159", "bid": "pwfVXwRezic", "__yadk_uid": "sSRJaB2vjBBkTfN6m7qK88sCxq9yiD5y",
        "_vwo_uuid_v2": "FFAFD09BFF20B3EB48CC2E5732174951|ced283bb85c6ec322963dd59f5188cfb", "ap": "1",
        "_pk_ref.100001.4cf6": "%5B%22%22%2C%22%22%2C1503235681%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D",
        "_pk_id.100001.4cf6": "5df75a257f8998e5.1498916085.6.1503235681.1503231672.", "_pk_ses.100001.4cf6": "*",
        "__utmt_douban": "1", "__utma": "30149280.1451420405.1498916085.1503233585.1503235681.11",
        "__utmb": "30149280.1.10.1503235681", "__utmc": "30149280",
        "__utma": "223695111.1318916198.1498916085.1503230049.1503235681.6",
        "__utmb": "223695111.0.10.1503235681", "__utmc": "223695111"}
    '''

    cookies = ""
    # 测试用例，找到Chrome文件夹下的webdriver插件的路径，为了下面模拟浏览器方法的调用
    # browser = webdriver.Chrome()
    # browser.get('http://www.baidu.com/')
    driver = webdriver.Chrome(
        executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver")

    def web_login(self):
        # 模拟登陆豆瓣
        self.driver.get("https://accounts.douban.com/login?source=movie")
        # 通过寻找登录栏的用户名、密码等属性，来完成input的位置检索和输入
        elem_user = self.driver.find_element_by_name("form_email")
        user_list = ['17854258235', '17854259004', '17854258236']
        user = choice(user_list)
        # elem_user.send_keys("17854258235")
        # elem_user.send_keys("17854259004")
        # elem_user.send_keys("17854258236")
        elem_user.send_keys(user)
        time.sleep(1.5)
        elem_pwd = self.driver.find_element_by_name("form_password")
        elem_pwd.send_keys("Shen1314")
        time.sleep(1.5)
        # 因为在登录几次之后会有输入验证码，需要手动输入，登录之前留够时间手动输入验证码，以完成登录
        self.driver.find_element_by_id("remember").click()
        time.sleep(10)
        self.driver.find_element_by_name("login").click()
        time.sleep(3)

        # 完成登录后直接跳转到目标电影页面
        # 测试用例，5942150，喜酒短评的‘看过’部分的短评为例
        #  self.driver.get("https://movie.douban.com/subject/5942150/comments?status=P")
        self.driver.get(self.url + '?status=P')
        time.sleep(5)
        cookiestr = ""
        for item in self.driver.get_cookies():
            name = item["name"]
            value = item["value"]
            cookiestr = cookiestr + '"' + name.replace('"', '') + '":"' + value.replace('"', '') + '", '
        # 摘取所需要的字段
        cookiestr = "{" + cookiestr[0:len(cookiestr) - 2] + "}"
        print(cookiestr)
        # cookiestr转为字典类型并传到cookies字典
        self.cookies = json.loads(cookiestr)

    def start_requests(self):
        self.web_login()
        # 测试是否获得到了cookies字典
        print(self.cookies)
        # 利用for循环，做好获取两种评论的所有cookie的准备
        for url in self.start_urls:
            # 获得豆瓣未登录状态下的合法的一个随机cookies字典中的bid属性的字符串值，用来迷惑反爬虫机制, bid=5jPFmAH6fdt
            # "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))
            self.cookies["bid"] = "".join(random.sample(string.ascii_letters + string.digits, 11))
            yield Request(url, headers=self.headers, cookies=self.cookies, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # 提取网页中‘下一页’的链接，href为链接的列表，虽然是列表，但是只有一个链接，即href[0]
        # xpath://div[@id='paginator']/a/@href,内容:?start=20&limit=20&sort=new_score&status=P&percent_type=,进行下页链接拼接
        # 链接不为空时，就每一页每一页的获取，callback=parse，相当于递归
        href = response.xpath("//div[@id='paginator']/a[@class='next']/@href").extract()

        for sel in response.css('div[class=comment-item]'):
            item = DoubanItem()
            # xpath://div[@id='content']/h1/text(),内容:喜酒 短评
            item['movie_name'] = response.css('div[id=content] h1::text').extract()[0]

            # xpath://div[@class='avatar']/a/@title 内容：每页的20个用户名
            item['user'] = sel.css('div[class=avatar] a::attr(title)').extract()[0]
            # xpath://div[@class='avatar']/a/@href 内容：每页的20个用户主页链接
            item['userlink'] = sel.css('div[class=avatar] a::attr(href)').extract()[0]
            # xpath://div[@class='comment']/h3/span[@class=''comment-info]/span 列表内容:0.看过/没看过，1.评分，2.评论的年月日
            infos = sel.css('div[class=comment] h3 span[class=comment-info] span')
            # 是否看过影片
            isView = infos[0].css('::text').extract()[0]
            item['isView'] = isView
            # 看过的情况下，有两种情况，评分和没评分，以及评论时间
            if isView == u'看过':
                # 无评分时
                if len(infos) == 2:
                    item['score'] = u"无评分"
                    # xpath://div[@class='comment']/h3/span[@class='comment-info']/span[2]/@title 列表内容：推荐
                    item['date'] = infos[1].css('::attr(title)').extract()[0]
                # 有评分时，长度为3
                else:
                    # xpath://div[@class='comment']/h3/span[@class='comment-info']/span[2]/@title 列表内容：推荐
                    item['score'] = infos[1].css('::attr(title)').extract()[0]
                    # xpath://div[@class='comment']/h3/span[@class='comment-info']/span[3]/@title 列表内容：2012-01-05 09:01:06
                    item['date'] = infos[2].css('::attr(title)').extract()[0]
            # 没看过的情况下，只有无评分和时间
            else:
                item['score'] = u"无评分"
                item['date'] = infos[1].css('::attr(title)').extract()[0]
            # xpath://div[@class='comment']/h3/span[@class='comment-vote']/span/text(),列表内容：认为有用人数
            item['support'] = sel.css('div[class=comment] h3 span[class=comment-vote] span::text').extract()[0]
            # xpath://div[@class='comment']/p/text() ,列表内容：每页的20个短评内容，需要处理，有换行符和空格
            item['content'] = sel.css('div[class=comment] p::text').extract()[0].replace('\n', '').rstrip()
            yield item

        if len(href) > 0 and href[0].strip() != "":
            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            # 生成每页随机cookies字典中的bid属性的字符串值，用来迷惑反爬虫机制, bid=5jPFmAH6fdt
            self.cookies["bid"] = "".join(random.sample(string.ascii_letters + string.digits, 11))
            # 在Request里面拼接url，进行每个评论网页的获取
            new_url = "https://movie.douban.com/subject/" + str(self.num) + "/comments"
            yield scrapy.Request(new_url + href[0], headers=self.headers,
                                 cookies=self.cookies, callback=self.parse)
            # 测试用，看是否进行了正确的跳转
            # yield scrapy.Request("https://movie.douban.com/subject/5942150/comments" + href[0], headers=self.headers, cookies=self.cookies, callback=self.parse)

