from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from theZoo.spiders.js_spider import JSSpider


process = CrawlerProcess(get_project_settings())
process.crawl(JSSpider)
process.start()