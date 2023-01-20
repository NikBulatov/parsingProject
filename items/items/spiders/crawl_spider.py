import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlSpiderSpider(CrawlSpider):
    name = 'crawl_spider'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_basic/']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths='//div[@class="card"]/a'),
            callback='parse_item',
            follow=True),
        Rule(
            LinkExtractor(
                restrict_xpaths='(//ul[@class="pagination"]/li)[last()]/a'),
            follow=True),
    )

    def parse_item(self, response):
        item = {}

        item['title'] = response.xpath(
            '//img[contains(@class, "card-img-top")]/@alt').get()
        item['price'] = response.xpath(
            '//div[@class="card-body"]/h4/text()').get()
        item['description'] = response.xpath(
            '//p[@class="card-text"]/text()').get()
        item['image'] = response.urljoin(
            response.xpath('//div[@class="card"]/img/@src').get())
        return item
