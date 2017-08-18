# -*- coding: utf-8 -*-

import pymongo
import txmongo
from txmongo.connection import ConnectionPool
from twisted.internet import defer
from txmongo.filter import sort
from scrapy.crawler import Crawler
from scrapy.exceptions import DropItem

from sm_save_html_source.items import SM_SaveHTMLSourceItem


class SM_SaveHTMLSourcePipeline(object):
    @classmethod
    def from_crawler(cls, crawler: Crawler):
        return cls(crawler)

    def __init__(self, crawler: Crawler):
        self.crawler = crawler
        self.settings = crawler.settings

    @defer.inlineCallbacks
    def open_spider(self, spider):
        # Sync
        # self.client = pymongo.MongoClient(self.settings['MONGODB_URI'])
        # self.db = self.client[self.settings['MONGODB_DB']]
        # self.coll = self.db[self.settings['MONGODB_COLL_RAW']]
        # self.coll.create_index('request_url')
        # Async
        self.client = yield ConnectionPool(self.settings['MONGODB_URI'])
        self.db = self.client[self.settings['MONGODB_DB']]
        self.coll = self.db[self.settings['MONGODB_COLL_RAW']]
        self.coll.create_index(sort([('request_url', 1)]))

    @defer.inlineCallbacks
    def close_spider(self, spider):
        # Sync
        # self.client.close()
        # Async
        yield self.client.disconnect()

    @defer.inlineCallbacks
    def process_item(self, item, spider):
        if isinstance(item, SM_SaveHTMLSourceItem):
            yield self.coll.update_one(
                {'request_url': item['request_url']},
                {'$set': dict(item)},
                upsert=True
            )
            raise DropItem
        else:
            return item


if __name__ == '__main__':
    pass
