#coding=utf-8
'''
Created on 2015年6月24日

@author: foxzhao
'''
import scrapy
from scrapy.utils.project import get_project_settings
from huaian.items import HuaianItem
# from scrapy.selector import Selector

import json
import urllib

class HuaianSpider(scrapy.Spider):
    name='soufun'
    allowed_domain=["fang.com"]
    start_urls=[]
    city=None
    
    def __init__(self, name=None, **kwargs):
        self.city = kwargs.get('city', 'shenzhen')
        super(HuaianSpider, self).__init__(name, **kwargs)
        self.initialize()
        
    def initialize(self):
        url_dict=get_project_settings().get('URL_DICT')
#         city=raw_input('which city you wanna scrapy?')
#         self.city = city
#        exit()
#       url="http://newhouse.huaian.fang.com/house/s/?x1=118.989043&x2=119.169854&y1=33.538872&y2=33.632707&strDistrict=&strRoundStation=&railway=&strPurpose=&strPrice=&strHuxing=&saling=&strStartDate=&isyouhui=&strOrderBy=&strKeyword=&railway_station=&strComarea=&housetag=&strSort=mobileyh&a=ajaxXfMapSearch&city=huaian&PageNo={}"
        url=url_dict[self.city]
        fp = urllib.urlopen(url.format(1))
        meta = json.loads(fp.read())
        pages = meta['pagenum']
        for num in range(1, pages + 1):
            self.start_urls.append(url.format(num))    
#     for i in range(1,35):
#         url="http://newhouse.huaian.fang.com/house/s/?x1=118.989043&x2=119.169854&y1=33.538872&y2=33.632707&strDistrict=&strRoundStation=&railway=&strPurpose=&strPrice=&strHuxing=&saling=&strStartDate=&isyouhui=&strOrderBy=&strKeyword=&railway_station=&strComarea=&housetag=&strSort=mobileyh&a=ajaxXfMapSearch&city=huaian&PageNo="+str(i)
#         start_urls.append(url)
#         
    def parse(self, response):
        content = json.loads(response.body)
        items = []
        for it in content['list']:
            item = HuaianItem()
            item['title'] = it['title']
            item['houseurl'] = it['houseurl']
            item['district'] = it['district']
            item['address'] = it['address']
            item['price_num'] = it['price_num']
            item['price_unit'] = it['price_unit']
            item['soufun_card_client'] = it['soufun_card_client']
            item['startTime_s'] = it['startTime_s']
            items.append(item)
            
        return items
    