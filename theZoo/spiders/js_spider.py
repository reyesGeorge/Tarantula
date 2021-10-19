import scrapy
from scrapy_splash import SplashRequest
from scrapy.spiders import CrawlSpider
from ..import items 


class JSSpider(CrawlSpider):
    name = "js"
    index = 0

    def start_requests(self):
                
        yield SplashRequest(url='http://quotes.toscrape.com/js/', callback=self.parse)


    def parse(self, response):
        item = items.ThezooItem()

        for quote in response.css('div.quote'):
            self.index += 1
            item["id"] = self.index
            item["text"] = quote.css('span.text::text').get()
            item["author"] = quote.css('small.author::text').get()
            item["tags"] = quote.css('div.tags a.tag::text').getall()
            item["spider"] = "JS"
            yield item
        
        print('Next Page')

        nav = response.css('ul.pager')
        next_page = nav.css('li.next a::attr(href)').get()
        print("NEXTPAGE!!!!!", next_page)

        if next_page:
            new_url = f'http://quotes.toscrape.com{next_page}'
            yield SplashRequest(
                url = new_url,
                callback= self.parse
            )
        else:
            print('No Pages Left')
            print("FINISHED")
            