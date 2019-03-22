# -*- coding:utf-8 -*-

from lxml import etree
import sys
import os

import requests
import urllib.request

class CrawJs:
    def getArticle (self, url):
        print('----- 开始爬取 -----')
        my_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6799.400 QQBrowser/10.3.2908.400'
        }
        # return requests.get(url=url, headers=my_headers)
        requset = urllib.request.Request(url=url, headers=my_headers)
        return urllib.request.urlopen(requset).read().decode('utf-8')

    def save (self, html):
        xml = etree.HTML(html)
        data = xml.xpath('//li/div[@class="content"]/a[@class="title"]/text()')
        for item in data:
            with open(os.path.join(sys.path[0], 'data.txt'), 'w') as f:
                f.write(item)

        print('----- 开始结束 -----')

if __name__ == '__main__':
    url = 'https://www.jianshu.com/'
    js = CrawJs()
    content = js.getArticle(url)
    js.save(content)
