import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NachiSpidersSpider(CrawlSpider):
    name = 'nachi_spiders'
    allowed_domains = ['nachi.org']
    start_urls = ['https://www.nachi.org/certified-inspectors/browse/us/']

    rules = (
        Rule(LinkExtractor(restrict_css='div.tabular tbody td a.no-underline.group'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield { 'FirstName': response.css('h1.m-0.mt-4::text').get().strip().split(' ')[0],
                'LastName': response.css('h1.m-0.mt-4::text').get().strip().split(' ')[1],
                'CompanyName': response.css('h2.m-0.mt-1.text-xl::text').get().strip(),
                'City':response.css('p.mt-4.font-serif.text-sm::text').get().strip().split(' ')[-2],
                'State':response.css('p.mt-4.font-serif.text-sm::text').get().strip().split(' ')[-1],
                'InterNACHI': [att.strip() for att in response.css('div.mb-8 p.font-mono::text').getall()],
                'OfficePhone':response.xpath('//*[@id="n-content"]/div/div/div[2]/div[2]/a/text()').get().strip(),
                'Website':  response.xpath('//*[@id="n-content"]/div/div/div[3]/div[1]/div[1]/p/a[2]/strong/text()').get(),
                'MobilePhone':[att.strip() for att in response.css('div.mt-2.tabular-nums:nth-child(3)::text').getall()],
                'Fax':[att.strip() for att in response.css('div.mt-2.tabular-nums:nth-child(4)::text').getall()]
                }

