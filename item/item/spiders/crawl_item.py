import scrapy
from scrapy.spiders import CrawlSpider
from scrapy_splash import SplashRequest


class CrawlItemSpider(CrawlSpider):
    name = 'crawl_item'
    allowed_domains = ['scrapingclub.com']
    # start_urls = ['https://scrapingclub.com/']

    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'

    script = f"""
        function main(splash, args)
          splash:set_user_agent('{USER_AGENT}')
          splash.private_mode_enabled = false
          
          assert(splash:go(args.url))
          assert(splash:wait(0.5))
          
          return {{
            html = splash:html(),
          }}
        end
    """

    def start_requests(self):
        yield SplashRequest(
            url='https://scrapingclub.com/exercise/detail_sign/',
            callback=self.parse,
            endpoint='execute',
            args={
                'lua_source': self.script,
            }
        )

    def parse(self, response):
        yield {
            'title': response.xpath('//h4[@class="card-title"]/text()').get(),
            'price': response.xpath('//h4[@class="card-price"]/text()').get(),
            'image': response.urljoin(
                response.xpath('//img[@class="card-img-top"]/@src').get()),
            'description': response.xpath(
                '//p[@class="card-description"]/text()').get()}
