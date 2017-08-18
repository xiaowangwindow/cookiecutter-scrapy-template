
import scrapy

class SM_SaveHTMLSourceItem(scrapy.Item):
    request_url = scrapy.Field()
    response_url = scrapy.Field()
    html = scrapy.Field()
    response_status = scrapy.Field()
    website = scrapy.Field()
    depth = scrapy.Field()


if __name__ == '__main__':
    pass
