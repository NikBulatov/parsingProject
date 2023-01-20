import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlBooksSpider(CrawlSpider):
    name = 'crawl_books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3/a'), callback='parse_item',
             follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[contains(text(), "next")]'),
             follow=True))

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//h1/text()').get()
        item['price'] = response.xpath('//p[@class="price_color"]/text()').get()
        item['description'] = response.xpath(
            '//div[@id="product_description"]/following-sibling::p/text()').get()
        return item
