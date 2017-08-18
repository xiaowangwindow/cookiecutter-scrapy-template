# -*- coding: utf-8 -*-
import re
from urllib.parse import urljoin

import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request, Response
from twisted.python.failure import Failure
from typing import AnyStr

from {{cookiecutter.project_name}}.items import RequestErrorItem
from {{cookiecutter.project_name}}.utils import url_util


class {{cookiecutter.spider_class}}(scrapy.Spider):
    name = '{{cookiecutter.spider_name}}'

    def start_requests(self):
        yield Request(
            '',
            meta={},
            callback=self.parse,
            errback=self.error_back,
        )

    def parse(self, response: Response):
        pass

    def error_back(self, failure: Failure):
        item = RequestErrorItem()
        item['request_url'] = failure.request.url
        item['error_detail'] = str(failure)
        yield item
