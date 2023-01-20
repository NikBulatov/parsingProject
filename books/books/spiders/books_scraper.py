import scrapy


class BooksScraperSpider(scrapy.Spider):
    name = 'books_scraper'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        articles = response.xpath('//article[@class="product_pod"]')

        for article in articles:
            title = article.xpath('.//h3/a/@title').get()
            image = response.urljoin(article.xpath(
                './/div[@class="image_container"]/a/img/@src').get())
            price = article.xpath('.//p[@class="price_color"]/text()').get()

            yield {
                'title': title,
                'price': price,
                'image': image
            }

        next_page = response.xpath('//a[contains(text(), "next")]')
        if next_page:
            next_page_url = response.urljoin(next_page.xpath('.//@href').get())
            yield scrapy.Request(url=next_page_url, callback=self.parse)
