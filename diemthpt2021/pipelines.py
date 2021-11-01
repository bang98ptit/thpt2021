# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi


class Diemthpt2021Pipeline:
    @classmethod
    def from_crawler(cls, crawler):
        cls.MYSQL_DB_NAME = crawler.settings.get("MYSQL_DB_NAME", 'scrapy_default')
        cls.HOST = crawler.settings.get("MYSQL_HOST", '127.0.0.1')
        cls.PORT = crawler.settings.get("MYSQL_PORT", 3306)
        cls.USER = crawler.settings.get("MYSQL_USER", 'root')
        cls.PASSWD = crawler.settings.get("MYSQL_PASSWORD", 'default')
        return cls()

    def open_spider(self, spider):
        self.dbpool = adbapi.ConnectionPool('pymysql', host=self.HOST, port=self.PORT, user=self.USER,
                                            passwd=self.PASSWD, db=self.MYSQL_DB_NAME, charset='utf8')

    def close_spider(self, spider):
        self.dbpool.close()

    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insert_db, item)

        return item

    def insert_db(self, tx, item):
        value = (
            item['ka00'],
            item['ka01'],
            item['kb00'],
            item['kc00'],
            item['codeNgoaiNgu'],
            item['kd01'],
            item['mDia'],
            item['mGdcd'],
            item['mHktn'],
            item['mHkxh'],
            item['mHoa'],
            item['mLy'],
            item['mNgoaiNgu'],
            item['mSinh'],
            item['mSu'],
            item['mToan'],
            item['mVan'],
            item['groupCode'],
            item['groupName'],
            item['schoolYear'],
            item['stt'],
            item['studentCode']
        )
        sql = 'INSERT INTO scores (ka00,ka01,kb00,kc00,codeNgoaiNgu,kd01,mDia,mGdcd,mHktn,mHkxh,mHoa,mLy,mNgoaiNgu,' \
              'mSinh,mSu,mToan,mVan,groupCode,groupName,schoolYear,stt,studentCode) values(%s, %s, %s, %s, %s,%s, %s, ' \
              '%s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s,%s)'


        tx.execute(sql, value)
