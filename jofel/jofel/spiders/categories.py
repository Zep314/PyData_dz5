import scrapy
import re


class CategoriesSpider(scrapy.Spider):
    name = "categories"
    allowed_domains = ["jofel.ru"]
    start_urls = ["https://jofel.ru/catalog/"]

    def parse(self, response):
        """
        Генерируем список ссылок на категории товаров сайта, указанного в response
        :param response: Адрес сайта
        :return: Вызываем обработчик для каждой категории товаров
        """
        categories = response.xpath('//div[@class="__content"]/h3/a')
        for category in categories:
            name = category.xpath('.//text()').get()
            link = category.xpath('.//@href').get()
            if name not in ('Акции', 'Новинки'):
                # Выкидываем эти две категории, т.к. в них товары повторяются
                yield response.follow(url=link, callback=self.parse_category)

    def parse_category(self, response):
        """
        Генерируем список ссылок на страницы с товарами в указанной категории
        :param response: Ссылка на категорию
        :return: Вызываем обработчик для каждого товара
        """
        pages = response.xpath("//a[@class='__full-link']")
        for page in pages:
            link = page.xpath('.//@href').get()
            yield response.follow(url=link, callback=self.parse_product)

        # Проверяем, есть ли ссылка на следующую страницу с товарами
        next_page = response.xpath("//a[@class='fontello-angle-double-right']")
        next_page_url = next_page.xpath('.//@href').get()
        if next_page_url:
            # Если следующая страница есть - вызываем обработчик снова
            yield response.follow(url=next_page_url, callback=self.parse_category)

    def parse_product(self, response):
        """
        Парсим данные с указанной страницы
        :param response: Адрес страницы с товаром
        :return: Словарь с данными со страницы
        """
        page_data = {  # Заполняем структуру, чтобы она сохранялась, если вдруг данные будут неполными
            'Category': None,
            'Name': None,
            'VendorCode': None,
            'Vendor': None,
            'Price_Eur': None,
            'Price_Rub': None,
            'Product_url': response.url,
            'Image_url': None,
        }
        try:
            page_data['Category'] = response.xpath("//ul[@class='breadcrumbs']/li/a/text()")[2].get()
        except (Exception,):
            pass
        try:
            page_data['Name'] = response.xpath("//h1[@class='__title h2']/text()")[0].get()
        except (Exception,):
            pass
        try:
            page_data['Image_url'] = response.urljoin(
                response.xpath("//figure[@class='__image __image--big']/a/@href").get())
        except (Exception,):
            pass
        try:
            characteristics = response.xpath("//div[@class='__line __line--info']/p/b/text()")
            page_data['VendorCode'] = characteristics[0].get()
            page_data['Vendor'] = characteristics[1].get()
        except (Exception,):
            pass
        try:
            page_data['Price_Eur'] = float("".join(re.findall('[0-9.,]',
                                                              response.xpath(
                                                                  "//div[@class='__line __line--price']/p/text()")[0].
                                                              get())).replace(',', '.'))
        except ValueError:
            pass
        try:
            page_data['Price_Rub'] = float("".join(re.findall('[0-9.,]',
                                                              response.xpath(
                                                                  "//div[@class='__line __line--price']/p/text()")[1].
                                                              get())).replace(',', '.'))
        except ValueError:
            pass
        yield page_data
