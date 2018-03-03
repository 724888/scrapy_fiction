# -*- coding: utf-8 -*-
import scrapy


class FictionItem(scrapy.Item):
    name = scrapy.Field()   #小说名字
    chapter_name = scrapy.Field()   #小说章节名字
    chapter_content = scrapy.Field()    #小说章节内容
    order_id = scrapy.Field()  #小说章节ID
