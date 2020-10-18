# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DoubanMovieItem(scrapy.Item):
    # 排名
    ranking = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评论人数
    score_num = scrapy.Field()

class NowcoderItem(scrapy.Item):
    # 工作名称
    title = scrapy.Field()
    # 公司名称
    company = scrapy.Field()
    # 工作地址
    address = scrapy.Field()
    # 薪资
    salary = scrapy.Field()

