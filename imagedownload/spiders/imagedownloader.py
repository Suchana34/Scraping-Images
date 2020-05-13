import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from imagedownload.items import ImagedownloadItem


class imageDownloader(scrapy.Spider):
    name = 'imgdownloader'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self,response):

        l = ItemLoader(item = ImagedownloadItem(), response=response)

        title = response.css('.product_pod a').css('::text').extract_first()
        image_urls = response.css('.thumbnail::attr(src)').extract_first()
        image_urls = image_urls.replace('../', 'http://books.toscrape.com/')

        l.add_value('title', title)
        l.add_value('image_urls', image_urls)

        yield l.load_item()

        #process next page
        next_page_url = response.css('.next a::attr(href)').extract_first()
        
        if next_page_url is not None:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse)
        
        

