import scrapy
import json
from ..import items 


class ScrollSpider(scrapy.Spider):
    name = "scroll"
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [api_url.format(1)]

    index = 0
    
    def parse(self, response):

        data = json.loads(response.text)

        item = items.ThezooItem()

        for quote in data['quotes']:
            self.index += 1
            item["id"] = self.index
            item["text"] = quote['text']
            item["author"] = quote['author']
            item["tags"] = quote['tags']
            item["spider"] = "Scroll"
            yield item
        
        print('Next Page')

        if data['has_next']:
            next_page = data['page'] + 1
        
            
            yield scrapy.Request(
                url = self.api_url.format(next_page),
                callback= self.parse
            )
        else:
            print('No Page Left')
            print("FINISHED")