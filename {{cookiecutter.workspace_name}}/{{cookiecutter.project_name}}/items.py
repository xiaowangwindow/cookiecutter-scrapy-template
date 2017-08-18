# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy{{cookiecutter.spider_class}}Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class RequestErrorItem(scrapy.Item):
    request_url = scrapy.Field()
    error_detail = scrapy.Field()
