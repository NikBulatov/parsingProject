import scrapy


class LogInSpider(scrapy.Spider):
    name = 'log_in'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.xpath("//input[@name='csrf_token']/@value").get()
        yield scrapy.FormRequest.from_response(
            response,
            formxpath='//form',  # путь до формы
            formdata={  # данные, которые передаём форме
                'username': 'admin',
                'password': 'admin',
                'csrf_token': csrf_token
            },
            callback=self.after_login,
        )

    def after_login(self, response):
        quotes = response.xpath('//div[@class="quote"]')

        for quote in quotes:
            yield {
                'author': quote.xpath('.//small[@class="author"]/text()').get(),
                'text': quote.xpath('.//span[@class="text"]/text()').get(),
                }
