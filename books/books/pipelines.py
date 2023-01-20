# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import sqlite3 as sql3


class BookPipelineMongoDB:
    # need two functions: before open and after closing

    def open_spider(self, spider):
        self._client = MongoClient('localhost', 27017)
        self._db = self._client['scrapy_books']

    def process_item(self, item, spider):  # how to write data
        self._db['all_books'].insert_one(item)
        return item

    def close_spider(self, spider):
        self._client.close()


class BookPipelineSQLite:
    def open_spider(self, spider):
        self._connection = sql3.connect('scrapy_book.db')
        self._cursor = self._connection.cursor()

        create_query = '''
        CREATE TABLE IF NOT EXISTS all_books(
            title TEXT,
            price TEXT,
            image TEXT
            )'''

        self._cursor.execute(create_query)
        self._connection.commit()

    def process_item(self, item, spider):  # function pass an item!
        insert_query = '''
        INSERT INTO all_books (title, price, image) VALUES (?, ?, ?)'''

        self._cursor.execute(insert_query, tuple(item.values())
                             # (
                             #      item.get('title'),
                             #      item.get('price'),
                             #      item.get('image'))
                             # )
                             )
        self._connection.commit()

        return item  # output in console

    def close_spider(self, spider):
        self._connection.close()
