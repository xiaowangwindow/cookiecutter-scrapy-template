# -*- coding: utf-8 -*-

import pymongo
from scrapy.crawler import Crawler
from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from {{cookiecutter.project_name}}.items import RequestErrorItem


class ScrapyCityPipeline(object):
    @classmethod
    def from_crawler(cls, crawler: Crawler):
        return cls(crawler)

    def __init__(self, crawler: Crawler):
        self.crawler = crawler
        self.settings = crawler.settings

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.settings['MONGODB_URI'])
        self.db = self.client[self.settings['MONGODB_DB']]
        self.error_coll = self.db[self.settings['MONGODB_COLL_ERROR']]
        self.error_coll.create_index('request_url')

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, RequestErrorItem):
            self.error_coll.update_one(
                {'request_url': item['request_url']},
                {'$set': dict(item)},
                upsert=True
            )
            raise DropItem
        else:
            return item
