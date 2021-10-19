import scrapy
from ..import items 


class DefaultSpider(scrapy.Spider):
    name = "quotes"
    index = 0

    def start_requests(self):
        
        yield scrapy.Request(url='http://quotes.toscrape.com', callback=self.parse)

    def parse(self, response):
        item = items.ThezooItem()

        for quote in response.css('div.quote'):
            self.index += 1
            item["id"] = self.index
            item["text"] = quote.css('span.text::text').get()
            item["author"] = quote.css('small.author::text').get()
            item["tags"] = quote.css('div.tags a.tag::text').getall()
            item["spider"] = "Default"
            yield item
        
        print('Next Page')

        nav = response.css('ul.pager')
        next_page = nav.css('li.next a::attr(href)').get()
        print("NEXTPAGE!!!!!", next_page)

        if next_page:
            new_url = f'http://quotes.toscrape.com{next_page}'
            yield scrapy.Request(
                url = new_url,
                callback= self.parse
            )
        else:
            print('No Pages Left')
            print("FINISHED")