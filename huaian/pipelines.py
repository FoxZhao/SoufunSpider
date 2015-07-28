# -*- coding: utf-8 -*-
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
# from os import path
import sqlite3
import xlwt
from xlwt.ExcelFormula import Formula

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# 写入CSV
class CsvWriterPipeline(object):
  
    def __init__(self):
        self.file = open('items.csv', 'w')
        self.file.write('楼盘名, 详细链接, 所属区, 详细地址,价格,单位,优惠,开盘时间'+'\n')
    def process_item(self, item, spider):
        # line = json.dumps(dict(item), ensure_ascii=False)  + "\n"
        values = []
        for key in ['title', 'houseurl', 'district', 'address','price_num','price_unit','soufun_card_client','startTime_s']:
            values.append(item[key] if item[key] else '')
        # print values
        self.file.write(','.join(values).encode('utf-8'))
        self.file.write('\n')
        return item

#写入sqlite
class SqliteWriterPipeline(object):
       
    def __init__(self):
        self.conn=None
        self.filename='soufun.sqlite'
        # self.tablename='huaian'
        self.initalized = False
        # dispatcher.connect(self.initalize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)
        
         
    def process_item(self,item,spider):
        if not self.initalized:
            self.initalize(spider.city)
#         self.conn.execute('insert into huaian values(?,?,?,?,?,?,?,?,?)',
        self.conn.execute('insert into '+self.tablename+' values(?,?,?,?,?,?,?,?,?)',
                          (None,item['title'],item['houseurl'],item['district'],item['address'],
                           item['price_num'],item['price_unit'],item['soufun_card_client'],item['startTime_s']))
        return item
    #初始化创建相关城市的表
    def initalize(self, tablename):
        self.tablename = tablename
        self.conn=sqlite3.connect(self.filename)
        sql=self.conn.execute("select count(*)  from sqlite_master where type='table' and name = ?", [self.tablename])
        temp=sql.fetchall()[0][0]
        if temp == 0:
            self.create_table()
        else:
            self.conn.execute("drop table "+self.tablename)
            self.create_table()
        self.initalized = True
        return self.conn
 
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn=None
             
    def create_table(self):
        conn=sqlite3.connect(self.filename)
        
        conn.execute("create table "+self.tablename+"(id integer primary key autoincrement,title,houseurl,district,address,price_num,price_unit,soufun_card_client,startTime_s)")
        conn.commit()
        return conn
            
#写入Excel
class ExcelWriterPipeline(object): 
    def __init__(self):
        self.filename='huaian.xls'
        print self.filename
        self.style()
        dispatcher.connect(self.initalize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)
        
    def style(self):
        f1= xlwt.Font() 
        f1.height= 20*20 
        f1.underline= xlwt.Font.UNDERLINE_SINGLE 
        f1.colour_index= 4 
        self.h_style= xlwt.XFStyle() 
        self.h_style.font= f1
        
        f2=xlwt.Font()
        f2.height=20*20
        self.nomal_style=xlwt.XFStyle()
        self.nomal_style.font=f2
        return self.h_style,self.nomal_style
        
           
    def initalize(self):  
        self.file_write=xlwt.Workbook()
        self.file_write_sheet=self.file_write.add_sheet('huaian', cell_overwrite_ok=True)
        self.lineno = 1
        f=xlwt.Font()
        f.height=20*20
        f.bold=True
        alignment = xlwt.Alignment()
        alignment.horz=xlwt.Alignment.HORZ_CENTER
        style=xlwt.XFStyle()
        style.font=f
        style.alignment=alignment
        row0 = [u'楼盘名',u'楼盘链接',u'所属区',u'详细地址',u'价格',u'单位',u'优惠',u'开盘时间']
        for n in range(0,len(row0)):
            self.file_write_sheet.write(0, n, row0[n],style)
    def finalize(self):
        self.file_write.save(self.filename)

            
    def process_item(self,item,spider):
        i = self.lineno
        self.file_write_sheet.write(i,0,item['title'],self.nomal_style)
#         self.file_write_sheet.write(i,1,item['houseurl'])
        self.file_write_sheet.write_merge(i,i,1,1,Formula('HYPERLINK'+"(\""+item['houseurl']+"\")"),self.h_style)
        self.file_write_sheet.write(i,2,item['district'],self.nomal_style)
        self.file_write_sheet.write(i,3,item['address'],self.nomal_style)
        self.file_write_sheet.write(i,4,item['price_num'],self.nomal_style)
        self.file_write_sheet.write(i,5,item['price_unit'] if item['price_unit'] else u'价格未定',self.nomal_style)
        self.file_write_sheet.write(i,6,item['soufun_card_client'] if item['soufun_card_client'] else u'无优惠',self.nomal_style)
        self.file_write_sheet.write(i,7,item['startTime_s'],self.nomal_style)
        self.lineno += 1
          

