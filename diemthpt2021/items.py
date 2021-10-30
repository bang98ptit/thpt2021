# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Diemthpt2021Item(scrapy.Item):
    ka00 = scrapy.Field()
    ka01 = scrapy.Field()
    kb00 = scrapy.Field()
    kc00 = scrapy.Field()
    codeNgoaiNgu = scrapy.Field()
    kd01 = scrapy.Field()
    mDia = scrapy.Field()
    mGdcd = scrapy.Field()
    mHktn = scrapy.Field()
    mHkxh = scrapy.Field()
    mHoa = scrapy.Field()
    mLy = scrapy.Field()
    mNgoaiNgu = scrapy.Field()
    mSinh = scrapy.Field()
    mSu = scrapy.Field()
    mToan = scrapy.Field()
    mVan = scrapy.Field()
    groupCode = scrapy.Field()
    groupName = scrapy.Field()
    schoolYear = scrapy.Field()
    stt = scrapy.Field()
    studentCode = scrapy.Field()
    response = scrapy.Field()