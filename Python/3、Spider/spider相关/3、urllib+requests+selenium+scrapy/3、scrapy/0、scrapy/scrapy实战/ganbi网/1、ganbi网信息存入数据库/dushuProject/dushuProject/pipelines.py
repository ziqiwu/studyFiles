# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql
from scrapy.utils.project import get_project_settings


class DushuprojectPipeline(object):
    def __init__(self):
        self.fp = open('../textFiles/ganbi.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        print(json.dumps(dict(item),ensure_ascii=False))
        self.fp.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
        return item

    def close_spider(self,item):
        self.fp.close()


class DushuprojectMySQLPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        self.host = settings.get('DB_HOST')
        self.port = settings.get('DB_PORT')
        self.user = settings.get('DB_USER')
        self.password = settings.get('DB_PASSWORD')
        self.db = settings.get('DB_DB')
        self.charset = settings.get('DB_CHARSET')

        self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,db=self.db,charset=self.charset)
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        sql = 'insert into ganbi_basic (title,pub_time,see,info_url,duration) values("%s","%s","%s","%s","%s")' % (item['title'],item['pub_time'],item['see'],item['info_url'],item['duration'])
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
