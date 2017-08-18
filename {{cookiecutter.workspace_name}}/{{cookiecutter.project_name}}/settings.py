# -*- coding: utf-8 -*-

# Scrapy settings for {{cookiecutter.project_name}} project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import platform

DEBUGGING = True if 'local' in platform.node().lower() else False

BOT_NAME = '{{cookiecutter.project_name}}'

SPIDER_MODULES = ['{{cookiecutter.project_name}}.spiders']
NEWSPIDER_MODULE = '{{cookiecutter.project_name}}.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = '{{cookiecutter.project_name}} (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 300

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 32
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
# 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
# 'Content-Type': 'application/json;charset=UTF-8',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'sm_save_html_source.raw.HTMLSourceMiddleware': None,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'dm_request_proxy_rotation.proxy.DownloaderProxy': 100,
}
# DOWNLOADERPROXY_ENABLED = False
# HTTP_PROXY = [
#     # 'http://10.255.0.2:57777',
#     'http://localhost:8080'
# ]
# HTTPS_PROXY = HTTP_PROXY

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'sm_save_html_source.pipelines.SM_SaveHTMLSourcePipeline': 1,
    '{{cookiecutter.project_name}}.pipelines_async.ScrapyCityPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = [301, 302, 304, 400, 403, 404, 500, 502, 503]
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

RETRY_TIMES = 1
DOWNLOAD_TIMEOUT = 10
# DEPTH_LIMIT = 1
# DEPTH_PRIORITY = -1

LOG_LEVEL = 'DEBUG' if DEBUGGING else 'INFO'
LOG_FORMATTER = 'custom_logformatter.logformatter.PoliteLogFormatter'

if DEBUGGING:
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_USER = None
    MONGODB_PASSWORD = None
else:
    # TODO
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_USER = None
    MONGODB_PASSWORD = None
    pass

MONGODB_DB = 'test'
MONGODB_COLL_RAW = 'scrapy_raw'
MONGODB_COLL_ERROR = 'scrapy_error'
MONGODB_URI = 'mongodb://{auth}{host}:{port}'.format(
    auth='{username}:{password}@'.format(username=MONGODB_USER, password=MONGODB_PASSWORD) if MONGODB_USER else '',
    host=MONGODB_HOST,
    port=MONGODB_PORT,
)
