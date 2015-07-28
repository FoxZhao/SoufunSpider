# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuaianItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    houseurl=scrapy.Field()
    district=scrapy.Field()
    address=scrapy.Field()
    price_num=scrapy.Field()
    price_unit=scrapy.Field()
    soufun_card_client=scrapy.Field()
    startTime_s=scrapy.Field()
