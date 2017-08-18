
from scrapy.crawler import Crawler
from sm_save_html_source.items import SM_SaveHTMLSourceItem
from scrapy.exceptions import NotConfigured
from scrapy.http import Request, Response

class HTMLSourceMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler: Crawler):
        # if not crawler.settings.getbool('{class_name}_ENABLED'.format(class_name=cls.__name__.upper())):
        #     raise NotConfigured
        return cls(crawler)

    def __init__(self, crawler: Crawler):
        pass

    def process_spider_input(self, response, spider):
        pass

    def process_spider_output(self, response: Response, result, spider):
        item = SM_SaveHTMLSourceItem()
        item['request_url'] = response.request.url
        item['response_url'] = response.url
        item['response_status'] = response.status
        item['html'] = response.text
        item['website'] = response.meta.get('website', '')
        item['depth'] = response.meta.get('depth', 0)
        yield item
        for r in result or ():
            yield r

    def process_spider_exception(self, response: Response, exception, spider):
        print(exception)
        pass


if __name__ == '__main__':
    pass