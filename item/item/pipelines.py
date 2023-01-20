# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3 as sql3


class ItemSQLitePipeline:

    def open_spider(self, spider):
        self._connection = sql3.connect('scrapy_book.db')
        self._cursor = self._connection.cursor()

        create_query = '''
            CREATE TABLE IF NOT EXISTS items(
                title TEXT,
                price TEXT,
                image TEXT,
                description TEXT
                )
        '''

        self._cursor.execute(create_query)
        self._connection.commit()

    def process_item(self, item, spider):
        insert_query = '''
            INSERT INTO items (title, 
                               price,
                               image,
                               description) VALUES (?, ?, ?, ?)
        '''
        self._cursor.execute(insert_query, tuple(item.values()))
        self._connection.commit()

        return item

    def close_spider(self, spider):
        self._connection.close()
