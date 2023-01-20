# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class ItemsPipeline:
    # need two functions: before open and after closing

    def open_spider(self, spider):
        self._client = MongoClient('localhost', 27017)
        self._db = self._client['scrapy_books']

    def process_item(self, item, spider):  # how to write data
        self._db['all_books'].insert_one(item)
        return item

    def close_spider(self, spider):
        self._client.close()
