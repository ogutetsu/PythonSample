import scrapy


class ScrapySpiderSpider(scrapy.Spider):
    name = 'scrapy_spider'
    allowed_domains = ['anond.hatelabo.jp']
    start_urls = ["https://anond.hatelabo.jp/"]

    def parse(self, response):
        for url in response.css('p.sectionfooter a::attr("href")'):
            yield response.follow(url)
        pass
