import base64
import re
from itertools import cycle
from urllib.parse import urlunparse
from urllib.request import _parse_proxy
from urllib.request import proxy_bypass

from scrapy.crawler import Crawler
from scrapy.exceptions import NotConfigured
from scrapy.http import Request
from scrapy.settings import Settings
from scrapy.utils.httpobj import urlparse_cached
from scrapy.utils.python import to_bytes
from typing import Tuple


class DownloaderProxy(object):
    @classmethod
    def from_crawler(cls, crawler: Crawler):
        if not crawler.settings.getbool('{class_name}_ENABLED'.format(class_name=cls.__name__.upper())):
            raise NotConfigured
        return cls(crawler)

    def __init__(self, crawler: Crawler):
        self.auth_encoding = crawler.settings.get('HTTPPROXY_AUTH_ENCODING', 'latin-1')
        self.proxies = self.getproxies(crawler.settings)

    def process_request(self, request: Request, spider):
        if 'proxy' in request.meta:
            if request.meta['proxy'] is None:
                return
            creds, proxy_url = self._get_proxy(request.meta['proxy'], '')
            request.meta['proxy'] = proxy_url
            if creds and not request.headers.get('Proxy-Authorization'):
                request.headers['Proxy-Authorization'] = b'Basic ' + creds
            return
        elif not self.proxies:
            return

        parsed = urlparse_cached(request)
        scheme = parsed.scheme

        if scheme in ('http', 'https') and proxy_bypass(parsed.hostname):
            return

        if scheme in self.proxies:
            self._set_proxy(request, scheme)

    def _basic_auth_header(self, username, password):
        user_pass = to_bytes(
            '{username}:{password}'.format(username=username, password=password),
            encoding=self.auth_encoding
        )
        return base64.b64encode(user_pass).strip()

    def _set_proxy(self, request: Request, scheme):
        creds, proxy = next(self.proxies[scheme])
        print((creds, proxy))
        request.meta['proxy'] = proxy
        if creds:
            request.headers['Proxy-Authorization'] = b'Basic ' + creds

    def _get_proxy(self, url, orig_type=''):
        proxy_type, user, password, hostport = _parse_proxy(url)
        proxy_url = urlunparse((proxy_type or orig_type, hostport, '', '', '', ''))

        creds = self._basic_auth_header(user, password) if user else None

        return creds, proxy_url

    def getproxies(self, settings: Settings):
        pattern = re.compile(r'(?P<scheme>[A-Z]+)_PROXY')

        def _filter(tuple_: Tuple):
            m = pattern.match(tuple_[0])
            if m:
                scheme = m.group('scheme').lower()
                return scheme, cycle([self._get_proxy(item, scheme) for item in tuple_[1]])

        proxies = []
        for item in settings.items():
            pair = _filter(item)
            if pair:
                proxies.append(pair)
        return dict(proxies)


if __name__ == '__main__':
    pass
