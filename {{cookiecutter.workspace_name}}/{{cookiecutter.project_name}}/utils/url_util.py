
import tldextract
from scrapy.link import Link
from urllib.parse import urlparse, urlunparse
from typing import List, AnyStr

Extracted_Links = List[Link]

def url_filter(link_list: Extracted_Links, home_url):

    ed_home = tldextract.extract(home_url)
    target_link_list = []
    for link in link_list:
        if link.url == home_url:
            continue
        o = urlparse(link.url)
        if o.path in ['/'] and not all(o[3:]):
            continue

        ed = tldextract.extract(link.url)
        if ed[1] == ed_home[1]:
            target_link_list.append(urlunparse((o.scheme, o.netloc, o.path, o.params, o.query, '')))
    return set(target_link_list)


def clean_url(url: AnyStr):
    if not url:
        return None
    o = urlparse(url)
    url = urlunparse(
        (o.scheme if o.scheme else 'http', o.netloc if o.netloc else o.path, o.path, o.params, o.query, o.fragment))
    o = urlparse(url)
    if o.netloc:
        return urlunparse((o.scheme if o.scheme else 'http', o.netloc, '', '', '', '')).lower()
    else:
        return None


if __name__ == '__main__':
    pass