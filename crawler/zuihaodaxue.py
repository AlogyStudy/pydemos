import requests
from bs4 import BeautifulSoup
import sys
import bs4


def getHTMLText(url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    try:
        zhdx = requests.get(url, headers=headers, timeout=30)
        # zhdx.encoding = 'utf-8'
        zhdx.encoding = zhdx.apparent_encoding
        return zhdx.text
    except:
        print('爬取错误')
        return ''

def fillUnivList(uList, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody', attrs={'class': 'hidden_zhpm'}).children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            uList.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])

def printUniv(uList, num):
    # print('Suc' + str(num))
    tmpl = '{0:^10}\t{1:{3}^10}}\t{2:^10}\t{3:^10}'
    print(tmpl.format('排名', '学校名称', '位置', '总分', chr(12288)))
    for i in range(num):
        u = uList[i]
        print(tmpl.format(u[0], u[1], u[2], u[3], chr(12288)))

def main():
    url = 'http://zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    
    uinfo = []
    text = getHTMLText(url)
    fillUnivList(uinfo, text)
    printUniv(uinfo, 5)


if __name__ == '__main__':
    main()
