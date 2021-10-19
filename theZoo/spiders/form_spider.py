import scrapy
from ..import items 


class FormSpider(scrapy.Spider):
    name = "form"
    index = 0

    login_url = "https://quotes.toscrape.com/login"

    def start_requests(self):
        yield scrapy.Request(url=self.login_url, callback=self.form_login)

    def form_login(self,response):
        token = response.css('input[name="csrf_token"]::attr(value)').extract_first()

        data = {
            'csrf_token': token,
            'username': "George",
            'password': "pass"
        }
        yield scrapy.FormRequest(url=self.login_url, formdata=data, callback=self.parse)

    def parse(self, response):
        item = items.ThezooItem()


        for quote in response.css('div.quote'):
            self.index += 1
            item["id"] = self.index
            item["text"] = quote.css('span.text::text').get()
            item["author"] = quote.css('small.author::text').get()
            item["tags"] = quote.css('div.tags a.tag::text').getall()
            item["spider"] = "Form"
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