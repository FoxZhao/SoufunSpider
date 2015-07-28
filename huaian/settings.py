# -*- coding: utf-8 -*-

# Scrapy settings for huaian project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
import os
from os.path import dirname
path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)

BOT_NAME = 'soufun'

SPIDER_MODULES = ['huaian.spiders']
NEWSPIDER_MODULE = 'huaian.spiders'
#设置下载的等待时间
DOWNLOAD_DELAY = 0.25

#取消默认的useragent,使用新的useragent
DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'huaian.spiders.random_useragent.RandomUserAgentMiddleware' :400
    }

#所谓cookies，是指某些网站为了辨别用户身份而储存在用户本地终端（Client Side）上的数据（通常经过加密），
#禁止cookies也就防止了可能使用cookies识别爬虫轨迹的网站得逞。
#使用：在settings.py中设置COOKIES_ENABLES=False。也就是不启用cookies middleware，不想web server发送cookies。
COOKIES_ENABLES=False

DEFAULT_ITEM_CLASS = 'huaian.items.HuaianItem'

ITEM_PIPELINES = {
#     'huaian.pipelines.CsvWriterPipeline': 1
    'huaian.pipelines.SqliteWriterPipeline':1
#     'huaian.pipelines.ExcelWriterPipeline':1
    
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'huaian (+http://www.yourdomain.com)'

URL_DICT={
    "huaian":"http://newhouse.huaian.fang.com/house/s/?x1=118.989043&x2=119.169854&y1=33.538872&y2=33.632707&strDistrict=&strRoundStation=&railway=&strPurpose=&strPrice=&strHuxing=&saling=&strStartDate=&isyouhui=&strOrderBy=&strKeyword=&railway_station=&strComarea=&housetag=&strSort=mobileyh&a=ajaxXfMapSearch&city=huaian&PageNo={}",
    "dongguan":"http://newhouse.dg.fang.com/house/s/?x1=113.401812&x2=114.033069&y1=22.835345&y2=23.25038&strDistrict=&strRoundStation=&railway=&strPurpose=&strPrice=&strHuxing=&saling=&strStartDate=&isyouhui=&strOrderBy=&strKeyword=&railway_station=&strComarea=&housetag=&strSort=mobileyh&a=ajaxXfMapSearch&city=dg&PageNo={}",
    "shenzhen":"http://newhouse.sz.fang.com/house/s/?x1=113.30273&x2=114.749218&y1=22.128853&y2=22.961983&strDistrict=&strRoundStation=&railway=&strPurpose=&strPrice=&strHuxing=&saling=&strStartDate=&isyouhui=&strOrderBy=&strKeyword=&railway_station=&strComarea=&housetag=&strSort=mobileyh&a=ajaxXfMapSearch&city=sz&PageNo={}",
    "guangzhou":"http://newhouse.gz.fang.com/house/s/?x1=111.861163&x2=114.754137&y1=22.570115&y2=23.667713&strDistrict=&strRoundStation=&railway=&strPurpose=&strPrice=&strHuxing=&saling=&strStartDate=&isyouhui=&strOrderBy=&strKeyword=&railway_station=&strComarea=&housetag=&strSort=mobileyh&a=ajaxXfMapSearch&city=gz&PageNo={}",
    "beijin":"http://newhouse.fang.com/house/s/?x1=114.949158&x2=117.842133&y1=39.471658&y2=40.385241&strDistrict=&strRoundStation=&railway=&strPurpose=&strPrice=&strHuxing=&saling=&strStartDate=&isyouhui=&strOrderBy=&strKeyword=&railway_station=&strComarea=&housetag=&strSort=mobileyh&a=ajaxXfMapSearch&city=bj&PageNo={}"
}
 
