# -*- coding: utf-8 -*-
import re
import time
from urllib import request, parse

import scrapy
import pymysql
from scrapy.utils.project import get_project_settings

class ParsedushuspiderSpider(scrapy.Spider):
    name = 'parseDushuSpider'
    allowed_domains = ['www.ganbi99.com']
    start_urls = []

    settings = get_project_settings()
    host = settings.get('DB_HOST')
    port = settings.get('DB_PORT')
    user = settings.get('DB_USER')
    password = settings.get('DB_PASSWORD')
    db = settings.get('DB_DB')
    charset = settings.get('DB_CHARSET')

    conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
    cursor = conn.cursor()


    sql = '''select *,cast(replace(see,',','') as UNSIGNED) from ganbi_basic  order by cast(replace(see,',','') as UNSIGNED) desc limit 500'''
    cursor.execute(sql)
    res = cursor.fetchall()
    # res = cursor.fetchmany(3)  # 前3条数据
    url_dict = {}
    for row in res:
        url_dict[row[4]] = row[1]
        start_urls.append(row[4])



    # 获取所有详情页url
    def parse(self, response):
        pattern = re.compile(r'<source src="(.*?)".*?/>', re.S)

        # srcName = spider_driver.find_element_by_xpath('//video[@id="vjsplayer_html5_api"]')
        source = response.text

        src_list = pattern.findall(source)  # .strip('\n')
        src = src_list[0].strip('"').replace('amp;', '')
        print('------------下载页：' + src)
        # print(src)
        # spider_driver.get(src)
        print('开始下载')
        print('------解码之前的url：:' + response.url)
        print('------解码之后的：' + parse.unquote(response.url))
        print('------对应关系：{}'.format(self.url_dict.get(parse.unquote(response.url))))
        # print('------url_dict:{}'.format(self.url_dict))
        # print('------解码之后的url'+self.url_dict.get(parse.unquote(resposne.url)))
        print('下载地址：' + src)
        try:
            filename = self.url_dict.get(parse.unquote(response.url).strip()) + '.mp4'
        except Exception:
            filename = str(time.time()) + '.mp4'
        try:
            request.urlretrieve(url=src, filename=filename)
        except Exception:
            print('下载失败%s')
        print('下载完成')
