#-*- encoding: utf-8 -*-

import os
import urllib.request

from scrapy.spiders import Spider

class ScutxiaoyuanSpider(Spider):
    name = "scutxiaoyuan"
    allowed_domains = ["scut.edu.cn"]
    start_urls = [ "http://www.scut.edu.cn/new/9284/list.htm" ]

    def parse(self, response):
        for sel in response.xpath('//table[@class="wp_editor_art_paste_table"]/tbody/tr/td/p/img/@src'):
            link = sel.extract()
            print(link)
            absolute_src = "http://www.scut.edu.cn" + link
            print(absolute_src)
            file_path = os.path.join(".\\pics", os.path.basename(link))
            print(file_path)
            urllib.request.urlretrieve(absolute_src, file_path)
