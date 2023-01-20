import scrapy
from scrapy_splash import SplashRequest


class SplashQuotesSpider(scrapy.Spider):
    name = 'splash_quotes'
    allowed_domains = ['quotes.toscrape.com']
    # start_urls = ['https://quotes.toscrape.com/']

    script_exmpl = '''
        function main(splash, args)
        
          splash:set_user_agent('')  меняем user-agent
          
          headers = { можно менять в заголовках
            'User-Agent': ''
          }
          splash:set_custom_headers(headers) и установить их
          splash.private_mode_enabled = false отключить приватный режим
          
          assert(splash:go(args.url))
          assert(splash:wait(0.5))
          return {
            html = splash:html(),
            }
        end
    '''

    script = '''
        function main(splash, args)
          assert(splash:go(args.url))
          assert(splash:wait(0.5))
          return {
            html = splash:html(),
            }
        end
    '''

    def start_requests(self):
        yield SplashRequest(
            url='https://quotes.toscrape.com/js/',
            callback=self.parse,  # обработчик
            endpoint='execute',  # выполнить
            args={
                'lua_source': self.script,  # скрипт
                'proxy': ''  # change proxy here and in docker
            }
        )

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")

        for quote in quotes:
            yield {
                'author': quote.xpath(".//small[@class='author']/text()").get(),
                'text': quote.xpath(".//span[@class='text']/text()").get(),
                'tags': [tag.xpath(".//text()").get() for tag in
                         quote.xpath(".//a[@class='tag']")]
            }

        next_page = response.xpath("//a[contains(text(), 'Next')]")
        if next_page:
            next_page_url = response.urljoin(next_page.xpath(".//@href").get())
            yield SplashRequest(
                url=next_page_url,
                callback=self.parse,
                endpoint='execute',
                args={
                    'lua_source': self.script
                }
            )
