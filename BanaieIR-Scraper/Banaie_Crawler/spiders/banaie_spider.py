# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from Banaie_Crawler.items import BanaieCrawlerItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import time
from requests import Request

class BanaieSpider(CrawlSpider):
    name = "banaieir"
    allowed_domains = ["www.banaie.ir"]
    start_urls = [    "http://www.banaie.ir/sitemap.html" ]
    rules = [Rule(LinkExtractor(allow=()), callback='parse_item', follow=True)]

    def parse_item(self, response):
        item = BanaieCrawlerItem()
        selector = response.selector
        item['title'] = selector.xpath('//a[@class="contentpagetitle"]/text()').extract()
        item['body'] = ' '.join([x.strip() for x in (selector.xpath('//div[@class="article-content"]//text()').extract())])
        # item['body'] = item['body'].replace('\"','').replace("\'",'').replace(u"«","").replace(u"»","").replace(",","").replace(u"انتهای پیام","")
        item['section'] = selector.xpath('//span[@class="article-section"]/a/text()').extract()
        item['category'] = selector.xpath('//span[@class="article-category"]/a/text()').extract()
        item['pubDate'] = selector.xpath('//span[@class="createdate"]/text()').extract()
        item["tags"] = []
        tags = selector.xpath('//p[@class="tags"]/a')
        if tags :
          for tag in tags :
             item["tags"].append(tag.xpath("text()").extract())
        yield item

    # def start_requests(self):
    #     headers= {"Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/47.0.2526.70 Mobile/13C71 Safari/601.1.46"}
    #     for url in self.start_urls:
    #         yield Request(url, headers=headers)