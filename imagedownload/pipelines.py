# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

class ImagedownloadPipeline:
    def process_item(self, item, spider):

        os.chdir('C:\\Users\\SUCHANA CHAKRABARTI\\Desktop\\downloading_images\\imagedownload\\images')

        for count in range(len(item)):
            if item['images'][0]['path'] is not None:
                
                new_name = item['title'][0] + '.jpg'
                new_path = 'full/' + new_name

                return os.rename(item['images'][0]['path'], new_path)