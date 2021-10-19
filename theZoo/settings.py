# Scrapy settings for theZoo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'theZoo'

SPIDER_MODULES = ['theZoo.spiders']
NEWSPIDER_MODULE = 'theZoo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'



# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# For Splash
SPLASH_URL = 'http://splash:8050'


# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# Enables stats shared based on Redis
STATS_CLASS = "scrapy_redis.stats.RedisStatsCollector"
# Specify the host and port to use when connecting to Redis (optional).
REDIS_HOST = 'redis'
REDIS_PORT = 6379
# Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True

### TO CLEAR THE CACHE FILTER UNCOMMENT THE BELOW SETTING
# SCHEDULER_FLUSH_ON_START=1


## For Scylla
# DOWNLOAD_TIMEOUT = 180
# RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 400, 429, 403, 404]
# # scrapy-scylla-proxies settings
# # Enabled
# SSP_ENABLED = True
# # Location of the scylla server
# SSP_SCYLLA_URI = 'http://localhost:8899'
# # Proxy timeout in seconds
# SSP_PROXY_TIMEOUT = 60
# # Get only https proxies
# SSP_HTTPS = True
# SSP_SPLASH_REQUEST_ENABLED = True


# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
#    'theZoo.middlewares.ThezooSpiderMiddleware': 543,
   'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,

}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'theZoo.middlewares.ThezooDownloaderMiddleware': 543,

   'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#    'theZoo.middlewares.ProxyMiddleware': 100,

   'scrapy_splash.SplashCookiesMiddleware': 723,
   'scrapy_splash.SplashMiddleware': 725,
   'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# w/out using redis you would use the below for Splash
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'theZoo.pipelines.ThezooPipeline': 300,
#    'scrapy_redis.pipelines.RedisPipeline': 300
}
DATABASE = {
    "drivername": "postgresql",
    "host": 'pg',
    "port": '5432',
    "username": 'user',
    "password": 'pass',
    "database": 'legalist',
}
LOG_LEVEL = "INFO"


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

