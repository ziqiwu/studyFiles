# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dushuProject.items import DushuItem


class DushuspiderSpider(CrawlSpider):
    name = 'dushuSpider'
    allowed_domains = ['www.ganbi99.com']
    # start_urls = ['https://www.ganbi99.com/videos/asian?page=1']
    start_urls = ['https://www.ganbi99.com/videos/asian']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.ganbi99.com/videos/asian'), callback='parse_item', follow = True),
        Rule(LinkExtractor(allow=r'https://www.ganbi99.com/videos/asian?page=\d+/'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        print(response.text)
        # with open('jilu.html','w',encoding='utf-8') as fp:
        #     fp.write(response.text)
        div_list = response.xpath('//div[@id="wrapper"]/div[1]/div[2]/div[1]/div[1]/div')

        for div in div_list:
            item = DushuItem()
            title = div.xpath('.//a/span/text()').extract_first()
            pub_time = div.xpath('./div/div[1]/text()').extract_first().strip()
            see = div.xpath('./div/div[2]/text()').extract_first().strip()
            info_url= 'https://www.ganbi99.com'+div.xpath('.//a/@href').extract_first()
            duration = div.xpath('.//span[@class="duration"]/text()').extract_first().strip()
            print(title)

            item['title'] = title
            item['pub_time'] = pub_time
            item['see'] = see
            item['info_url'] = info_url
            item['duration'] = duration
            # item_arr.append(item)
            yield item

