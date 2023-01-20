import scrapy


class LogInSpider(scrapy.Spider):
    name = 'log_in_dz'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/basic_login/']

    def parse(self, response):
        csrf_token = response.xpath(
            "//input[@name='csrfmiddlewaretoken']/@value").get()

        login, password = response.xpath('//code/text()')

        yield scrapy.FormRequest.from_response(
            response,
            formxpath='//form',
            formdata={
                'name': login.get(),
                'password': password.get(),
                'csrf_token': csrf_token
            },
            callback=self.after_login,
        )

    def after_login(self, response):
        success_message = response.xpath(
            '//div[@class="mt-4 my-4"]/p/text()').get()

        print(f'\x1b[6;30;42m {success_message} \x1b[0m')

        yield {'result': success_message}
