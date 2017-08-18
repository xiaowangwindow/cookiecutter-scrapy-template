import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def run():
    process = CrawlerProcess(get_project_settings())
    process.crawl('{{cookiecutter.spider_name}}')
    process.start()


if __name__ == '__main__':
    run()
