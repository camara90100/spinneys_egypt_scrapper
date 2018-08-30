# -*- coding: utf-8 -*-
import scrapy
from ..items import SpinneysscraperItem
class SpinneysSpider(scrapy.Spider):
    name = 'spinneys'
    allowed_domains = ['www.spinneys-egypt.com']

    def start_requests(self):
        urls = [
        "https://www.spinneys-egypt.com/en-us/spinneys/pro-chilld-food/promotions-details/pro-chilld-food",
        "https://www.spinneys-egypt.com/en-us/spinneys/pro-dry-food1/promotions-details/pro-dry-food1",
        "https://www.spinneys-egypt.com/en-us/spinneys/pro-dry-food1/promotions-details/fresh-food",
        "https://www.spinneys-egypt.com/en-us/spinneys/pro-non-food/promotions-details/pro-non-food",
        "https://www.spinneys-egypt.com/en-us/spinneys/pro-electronic/promotions-details/pro-electronic",
        "https://www.spinneys-egypt.com/en-us/spinneys/pro-textile/promotions-details/pro-textile",
        "https://www.spinneys-egypt.com/en-us/spinneys/pro-huose-hold/promotions-details/pro-huose-hold"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def extract_category(self, response):
        self.log("extracting category at " + response.url)
        # the right category should be the active one.
        for li in response.css('li.cat'):
            if li.css('a.active'):
                return li.css('span::text').extract_first().strip()
    
    def extract_products(self, response, category):           
        self.log("extracting product at " + response.url)


    def parse(self, response):
        self.log("parse at " + response.url)
        category = self.extract_category(response)
        for product in response.css('.Image_Wrapper'):
            img = response.url + product.css('a').css('img::attr(src)').extract_first()
            name = product.css('div.desc').css('h1::text').extract_first().strip()
            price_before = product.css('div.price').css('span.before::text').extract_first().strip()
            price_after = product.css('div.price').css('span.after::text').extract_first().strip()
            yield SpinneysscraperItem({
                "name": name,
                "price_before": price_before,
                "price_after": price_after,
                "img": img,
                "category": category
            })