# -*- coding: utf-8 -*-
import scrapy
from time import sleep


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["sh.lianjia.com"]
    start_urls = (
        'http://sh.lianjia.com/zufang/pudongxinqu/l1z2',
        'http://sh.lianjia.com/zufang/xuhui/l1z2'
    )

    def parse(self, response):
        houses = response.xpath("//ul[@class='house-lst']/li")
        url = "http://sh.lianjia.com"
        for i in houses:
            item = dict()
            item['title'] = i.xpath(".//div[@class='info-panel']/h2/a/text()").extract()[0]
            item['community'] = i.xpath(".//div[@class='where']/a/span/text()").extract()[0]
            item['location'] = i.xpath(".//div[@class='other']/div[@class='con']/a/text()").extract()[1]
            item['floor'] = i.xpath(".//div[@class='other']/div[@class='con']/text()").extract()[3].strip()
            item['price'] = i.xpath(".//div[@class='price']/span[@class='num']/text()").extract()[0]
            item['url'] = url + i.xpath(".//div[@class='pic-panel']/a/@href").extract()[0]
            yield item

        next_page = response.xpath("//a[@gahref='results_next_page']/@href").extract()
        if next_page:
            next_url = url + next_page[0]
            sleep(1)
            yield scrapy.Request(url=next_url, callback=self.parse)
