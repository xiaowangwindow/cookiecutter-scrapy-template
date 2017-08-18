
import pymongo
from scrapy.crawler import Crawler
from scrapy.exceptions import DropItem
from txmongo.connection import ConnectionPool
from twisted.internet import defer, reactor, ssl
from txmongo.filter import sort

from {{cookiecutter.project_name}}.items import RequestErrorItem

class ScrapyCityPipeline(object):
    @classmethod
    def from_crawler(cls, crawler: Crawler):
        return cls(crawler)

    def __init__(self, crawler: Crawler):
        self.crawler = crawler
        self.settings = crawler.settings

    @defer.inlineCallbacks
    def open_spider(self, spider):
        self.client = yield ConnectionPool(self.settings['MONGODB_URI'])
        self.db = self.client[self.settings['MONGODB_DB']]
        self.error_coll = self.db[self.settings['MONGODB_COLL_ERROR']]
        yield self.error_coll.create_index(sort([('request_url', 1)]))


    @defer.inlineCallbacks
    def close_spider(self, spider):
        yield self.client.disconnect()

    @defer.inlineCallbacks
    def process_item(self, item, spider):
        if isinstance(item, RequestErrorItem):
            yield self.error_coll.update_one(
                {'request_url': item['request_url']},
                {'$set': dict(item)},
                upsert=True
            )
            raise DropItem
        else:
            return item

if __name__ == '__main__':
    pass