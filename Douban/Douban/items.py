# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影名
    movie_name = scrapy.Field()
    # 用户名
    user = scrapy.Field()
    # 用户主页
    userlink = scrapy.Field()
    # 是否看过
    isView = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评分日期
    date = scrapy.Field()
    # 支持数
    support = scrapy.Field()
    # 内容
    content = scrapy.Field()
    pass
