# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.settings import Settings
from scrapy.exceptions import DropItem
import logging

class Matches_of_weekPipeline(object):

    collection_matches = 'Week_matchesDB'

    def __init__(self,mongo_uri, mongo_db):
        # connection = pymongo.MongoClient(
        #     Settings['MONGODB_SERVER'],
        #     Settings['MONGODB_PORT']
        # )
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

        # db = connection[Settings['MONGODB_DB']]
        # self.collection = db[Settings['MONGODB_COLLECTION']]

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri= crawler.settings.get('MONGODB_URI'),
            mongo_db = crawler.settings.get('MONGODB_DB')
        )
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()
    

    def process_item(self, item, spider):
        self.db[self.collection_matches].insert(dict(item))
        logging.debug("Match added")
        return item