# Сбор и разметка данных (семинары)
## Урок 5. Scrapy

### Задание

1. Найдите сайт, содержащий интересующий вас список или каталог. Это может быть список книг, фильмов, спортивных 
   команд или что-то еще, что вас заинтересовало.
2. Создайте новый проект Scrapy и определите нового паука. С помощью атрибута start_urls укажите URL выбранной 
   вами веб-страницы.
3. Определите метод парсинга для извлечения интересующих вас данных. Используйте селекторы XPath или CSS для 
   навигации по HTML и извлечения данных. Возможно, потребуется извлечь данные с нескольких страниц или перейти 
   по ссылкам на другие страницы.
4. Сохраните извлеченные данные в структурированном формате. Вы можете использовать оператор yield для возврата 
   данных из паука, которые Scrapy может записать в файл в выбранном вами формате (например, JSON или CSV).
5. Конечным результатом работы должен быть код Scrapy Spider, а также пример выходных данных. Не забывайте соблюдать 
   правила robots.txt и условия обслуживания веб-сайта, а также ответственно подходите к использованию веб-скрейпинга.


### Решение

Устанавливаем scrapy, и создаем новый проект

    venv/bin/activate.bat
    pip install scrapy
    scrapy startproject jofel

Генерируем нового паука

    cd jofel/jofel/spiders/
    scrapy genspider categories "jofel.ru/catalog/"

Редактируем код паука: [jofel/jofel/spiders/categories.py](jofel/jofel/spiders/categories.py)

Запускае паука в работу:

    cd jofel
    scrapy crawl categories -o output.json

#### Результат работы:


Файл с данными: [jofel/output.json](jofel/output.json)

Вывод программы:

    (venv) C:\Work\python\Data\PyData_dz5\jofel>scrapy crawl categories -o output.json
    2024-01-16 15:40:27 [scrapy.utils.log] INFO: Scrapy 2.11.0 started (bot: jofel)
    2024-01-16 15:40:27 [scrapy.utils.log] INFO: Versions: lxml 5.1.0.0, libxml2 2.10.3, cssselect 1.2.0, parsel 1.8.1, w3lib 2.1.2, Twisted 22.10.0, Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)], pyOpenSSL 23.3.0 (OpenSSL 3.1.4 24 Oct 2023), cryptography 41.0.7, Platform Windows-10-10.0.22621-SP0
    2024-01-16 15:40:27 [scrapy.addons] INFO: Enabled addons:
    []
    2024-01-16 15:40:27 [asyncio] DEBUG: Using selector: SelectSelector
    2024-01-16 15:40:27 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.asyncioreactor.AsyncioSelectorReactor
    2024-01-16 15:40:27 [scrapy.utils.log] DEBUG: Using asyncio event loop: asyncio.windows_events._WindowsSelectorEventLoop
    2024-01-16 15:40:27 [scrapy.extensions.telnet] INFO: Telnet Password: cd16a05891d39273
    2024-01-16 15:40:27 [scrapy.middleware] INFO: Enabled extensions:
    ['scrapy.extensions.corestats.CoreStats',
     'scrapy.extensions.telnet.TelnetConsole',
     'scrapy.extensions.feedexport.FeedExporter',
     'scrapy.extensions.logstats.LogStats']
    2024-01-16 15:40:27 [scrapy.crawler] INFO: Overridden settings:
    {'BOT_NAME': 'jofel',
     'DOWNLOAD_DELAY': 0.1,
     'FEED_EXPORT_ENCODING': 'utf-8',
     'NEWSPIDER_MODULE': 'jofel.spiders',
     'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
     'SPIDER_MODULES': ['jofel.spiders'],
     'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'}
    2024-01-16 15:40:27 [scrapy.middleware] INFO: Enabled downloader middlewares:
    ['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
     'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
     'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
     'scrapy.downloadermiddlewares.retry.RetryMiddleware',
     'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
     'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
     'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
     'scrapy.downloadermiddlewares.stats.DownloaderStats']
    2024-01-16 15:40:27 [scrapy.middleware] INFO: Enabled spider middlewares:
    ['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
     'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
     'scrapy.spidermiddlewares.referer.RefererMiddleware',
     'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
     'scrapy.spidermiddlewares.depth.DepthMiddleware']
    2024-01-16 15:40:27 [scrapy.middleware] INFO: Enabled item pipelines:
    []
    2024-01-16 15:40:27 [scrapy.core.engine] INFO: Spider opened
    2024-01-16 15:40:27 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
    2024-01-16 15:40:27 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
    2024-01-16 15:40:27 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/> (referer: None)
    2024-01-16 15:40:27 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/bumagnye_izdeliya/> (referer: https://jofel.ru/catalog/)
    2024-01-16 15:40:27 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/prochie_acsessuary/> (referer: https://jofel.ru/catalog/)
    2024-01-16 15:40:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/pelenalnye_stoliky/> (referer: https://jofel.ru/catalog/)
    2024-01-16 15:40:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/auto_osvegitely_vozduha/> (referer: https://jofel.ru/catalog/)
    2024-01-16 15:40:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/ershiky_dlya_unitaza/> (referer: https://jofel.ru/catalog/)
    2024-01-16 15:40:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/poruchny/> (referer: https://jofel.ru/catalog/)
    2024-01-16 15:40:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/elektrolovushky/> (referer: https://jofel.ru/catalog/)
    2024-01-16 15:40:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/urny-vedra/> (referer: https://jofel.ru/catalog/)
    2024-01-16 15:40:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/dispensery/> (referer: https://jofel.ru/catalog/)
    2024-01-16 15:40:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/dozatory_dlya_myla/> (referer: https://jofel.ru/catalog/)
    2024-01-16 15:40:29 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/feny/> (referer: https://jofel.ru/catalog/)
    2024-01-16 15:40:29 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/elekrosushilki/> (referer: https://jofel.ru/catalog/)
    2024-01-16 15:40:29 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/bumagnye_izdeliya/pokrytiya_bumazhnye_na_sidene_unitaza_jofel_smennyy_blok_dlya_dispensera_am21000_21500_125_l_blok_ts/> (referer: https://jofel.ru/catalog/bumagnye_izdeliya/)
    2024-01-16 15:40:29 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/prochie_acsessuary/kryuchok_jofel_d_polotenets_dvoynoy_30_110_40_mm_nerzh_stal_aisi_304_polirov_pov_t/> (referer: https://jofel.ru/catalog/prochie_acsessuary/)
    2024-01-16 15:40:29 [scrapy.core.scraper] DEBUG: Scraped from <200 https://jofel.ru/catalog/bumagnye_izdeliya/pokrytiya_bumazhnye_na_sidene_unitaza_jofel_smennyy_blok_dlya_dispensera_am21000_21500_125_l_blok_ts/>
    {'Category': 'Бумажные изделия', 'Name': 'Покрытия бумажные на сиденье унитаза Jofel', 'VendorCode': 'AM20040', 'Vendor': 'Jofel', 'Price_Eur': 6.7, 'Price_Rub': 737.0, 'Product_url': 'https://jofel.ru/catalog/bumagnye_izdeliya/pokrytiya_bumazhnye_na_sidene_unitaza_jofel_smennyy_blok_dlya_dispensera_am21000_21500_125_l_blok_ts/', 'Image_url': 'https://jofel.ru/upload/iblock/98d/98dfae322c343f7238a6b906c3a9d519.jpg'}
    2024-01-16 15:40:29 [scrapy.core.scraper] DEBUG: Scraped from <200 https://jofel.ru/catalog/prochie_acsessuary/kryuchok_jofel_d_polotenets_dvoynoy_30_110_40_mm_nerzh_stal_aisi_304_polirov_pov_t/>
    
    ...
    
    2024-01-16 15:40:51 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://jofel.ru/catalog/auto_osvegitely_vozduha/aerozol_jofel_osvezhitel_vozdukha_d_dozatora_aromat_aloe_dlya_tualeta_ballon_250_ml/> (referer: https://jofel.ru/catalog/auto_osvegitely_vozduha/)
    2024-01-16 15:40:51 [scrapy.core.scraper] DEBUG: Scraped from <200 https://jofel.ru/catalog/auto_osvegitely_vozduha/aerozol_jofel_osvezhitel_vozdukha_d_dozatora_aromat_aloe_dlya_tualeta_ballon_250_ml/>
    {'Category': 'Автоматические освежители воздуха', 'Name': 'Аэрозоль Jofel - освежитель  воздуха для дозатора', 'VendorCode': 'AKA2016', 'Vendor': 'Jofel', 'Price_Eur': 7.4, 'Price_Rub': 814.0, 'Product_url': 'https://jofel.ru/catalog/auto_osvegitely_vozduha/aerozol_jofel_osvezhitel_vozdukha_d_dozatora_aromat_aloe_dlya_tualeta_ballon_250_ml/', 'Image_url': 'https://jofel.ru/upload/iblock/b10/b107b110eae4e2622916a73af96823f3.jpg'}
    2024-01-16 15:40:51 [scrapy.core.engine] INFO: Closing spider (finished)
    2024-01-16 15:40:51 [scrapy.extensions.feedexport] INFO: Stored json feed (174 items) in: output.json
    2024-01-16 15:40:51 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
    {'downloader/request_bytes': 88287,
     'downloader/request_count': 192,
     'downloader/request_method_count/GET': 192,
     'downloader/response_bytes': 5667772,
     'downloader/response_count': 192,
     'downloader/response_status_count/200': 192,
     'elapsed_time_seconds': 24.483823,
     'feedexport/success_count/FileFeedStorage': 1,
     'finish_reason': 'finished',
     'finish_time': datetime.datetime(2024, 1, 16, 12, 40, 51, 847416, tzinfo=datetime.timezone.utc),
     'httpcompression/response_bytes': 33397100,
     'httpcompression/response_count': 192,
     'item_scraped_count': 174,
     'log_count/DEBUG': 369,
     'log_count/INFO': 11,
     'request_depth_max': 4,
     'response_received_count': 192,
     'scheduler/dequeued': 192,
     'scheduler/dequeued/memory': 192,
     'scheduler/enqueued': 192,
     'scheduler/enqueued/memory': 192,
     'start_time': datetime.datetime(2024, 1, 16, 12, 40, 27, 363593, tzinfo=datetime.timezone.utc)}
    2024-01-16 15:40:51 [scrapy.core.engine] INFO: Spider closed (finished)
    
    (venv) C:\Work\python\Data\PyData_dz5\jofel>
