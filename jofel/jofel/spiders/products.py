import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["jofel.ru"]
    start_urls = ["https://jofel.ru/catalog/"]

    def parse(self, response):
        pass
