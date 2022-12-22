import scrapy
from scrapy import Request, FormRequest

class QuoteSpiderSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quotes.com']
    start_urls = ['https://quotes.toscrape.com/']


    def parse_login(self, response):
        ret = FormRequest.from_response(response, formdata={'username':'bigfredoh', 'password':'u10ce1079'})
        self.log("Sent:" + str(ret.body))
        return ret


    def start_requests(self):
        return [Request('https://quotes.toscrape.com/login', callback=self.parse_login)]

    def parse(self, response, **kwargs):
        pass