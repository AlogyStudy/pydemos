## 相关信息

- `Robots.txt`协议，网络爬虫排除标准。
    作用：网站告知网络爬虫哪些页面可以抓取，哪些不行。
    形式：在网站根目录下的`robots.txt`文件中规定。

```
User-agent: *  # 所有的网络爬虫都应该遵循如下协议
Disallow: /?* # 不允许访问以？开头都卢金
Disallow: /pop/*.html # 任何爬虫都不允许访问/pop/*.html
Disallow: /pinpai/*.html?*   # 符合这个定义规则的也不允许访问。

# 底下四个爬虫，不允许爬取任何资源。
User-agent: EtaoSpider 
Disallow: / 
User-agent: HuihuiSpider 
Disallow: / 
User-agent: GwdangSpider 
Disallow: / 
User-agent: WochachaSpider 
Disallow: /
```

`Robots`协议的使用：
网络爬虫：自动或人工识别robots.txt,再进行内容爬取。
约束性：`Robots`协议是建议但非约束性，网络爬虫可以不遵守，但存在法律风险。

类似人类访问的行为，访问次数很小，可以不遵守`Robots`协议。

> 爬虫常用相关库

获取：
- `import requests`
- `from urllib import request`
- `import scrapy`

解析：
- `from bs4 import BeautifulSoup`
- `from lxml import etree`
- `import jsonpath`
- `import re`

- `import http.cookiejar`
- `import aiohttp`
- `import asyncio`

## Requests

自动爬取HTML页面，自动网络请求提交。

基于`urllib`,比`urllib`方便，可以节约大量的工作，完全满足HTTP测试需求。
`Python`实现的简单易用的HTTP库。

```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

res = requests.get('url', hreaders=hreaders)
res.encoding = 'utf-8'
res.apparent_encoding = 'utf-8'
print(res.text)
```

带参数`GET`请求和解析`json`:
```python
import requests
import json

data = {
    'name': 't',
    'age': 2
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

resGet = requests.get('url', params=data)
resPost = requests.post('url', data=data, headers=headers)
print(resGet.text)
print(resGet.json())
print(json.loads(resGet.text))
print(resPost.json())
```

获取二进制数据和cookie：
```python
import requests

res = requests.get('https://github.com/favicon.ico')
print(type(res.text), 'res')
# <class 'str'>
print(type(res.content), 'content')
# <class 'bytes'>
print(res.cookies)

for key, value in res.cookies.items():
    print(key + '--' + value)

with open('fa.ico', 'wb') as f:
    f.write(res.content)
```

文件上传：
```python
import requests

files = {'file': open('./f.ico', 'rb')}
res = requests.post('http://httpbin.org/post', files=files)
print(res.text)
```
保持会话：
```python
import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)
```
验证证书：
```python
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
```
-----
```python
import requrests

response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
print(response.status_code)
```
代理设置：
```python
import requests
proxy = {
    'http': 'socks5://127.0.0.1:9742',
    'https': 'socks5://127.0.0.1:9742'
}

res = requests.get(url, proxies=proxy)
```
超时设置：
```python
import requests

from requests.exceptions import ReadTimeout

try:
    res = requests.get('http://httpbin.org/get', timetou=0.5)
    print(res.status_code)
except ReadTimeout:
    print('timeout')
```
认证设置：
```python
import requests
from requests.auth import HTTPBasicAuth

# res = requests.get('url', auth=HTTPBasicAuth('user', '123'))
res = requests.get('url', auth=('user', '123'))
print(res.status_code)
```
异常：
`requests.ConnectionError`: 网络连接错误，如DNS查询失败，拒绝连接等。
`requests.HTTPError`: HTTP错误异常。
`requests.URLRequired`: URL缺失异常。
`requests.TooManyRedirects`: 超过最大重定向次数，产生重定向异常。
`requests.ConnectTimeout`: 连接远程服务器超时异常。
`requests.Timeout`: 请求URL超时，产生超时异常。

操作之间都是独立无状态的。
`http`的世界中，网络通道跟服务器都是黑盒子。
能看到的就是url链接和对url链接进行的操作。

`PATCH`方法和`PUT`方法的区别：
假设URL位置有一组数据UserInfo，包括UserId，UserName，等20个字段。
需求：用户更改UserName，其它的用户信息没有更新。

使用`PATCH`方法，向URL提供修改的值UserName即可。节省网络带宽。
使用`PUT`，必须将所有的20个字段，一并提交URL参数，未提交字段删除。

网络爬虫的尺寸：
- 爬取网页，玩转网页。小规模，数据量小，爬取速度不敏感。可以使用`requests`，`urllib`库。占90%以上的比例。
- 爬取网站，爬取系列网站。中规模，数据量比较大，爬取速度敏感。可以使用`Scrapy`库
- 爬取全网。大规模，搜索引擎，爬取速度关键。

网络爬虫带来的风险问题：
- 骚扰问题：网络爬虫将会为web服务器带来巨大的资源开销。
- 法律问题：服务器上的数据有产权归属，会带来法律风险。
- 隐私问题

网络爬虫的限制：
- 来源限制：判断`User-Agent`进行限制。检查来访问HTTP协议头的`User-Agent`，只响应浏览器或友好爬虫的访问。
- 发布公告：`Robots`协议。


## Urllib

```python
# py2
import urllib2
res = urllib2.open('url')

# py3
import urllib.request
res = urllib.request.urlopen('url')
```

`get`请求：
```python
import urllib.request
res = urllib.request.urlopen('http:/www.baidu.com')
print(res.read().decode('utf-8'))
```
`post`请求：
```python
import urllib.request
import urllib.parse


data = bytes(urllib.parse.urlencode({'hello': 'world'}), encoding='utf-8')
res = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(res.read().decode('utf-8'))
```
`post`请求携带请求头：
```python
from urllib import request, parse

headers = {
    'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
    'Host': 'httpbin.org'
}
data = bytes(parse.urlencode({'hello': 'wrold'}), encoding='utf-8')
req = request.Requests(url=url, data=data, headers=headers, methods='POST')
# req.add_header('User-Agent', 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
```
设置代理：
```python
from urllib import request


proxy_handler = request.ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})

opener = request.build_opener(proxy_handler)
resp = opener.open('http://www.baidu.com')
print(resp.read())
```

## bs4

bs4基本类型：
- `Tag`, `soup.a`: 标签，最基本的信息组织单元。
- `Name`, `soup.name`: 标签的名字。
- `Attributes`, `soup.attrs`: 标签的属性。
- `NavigableString`, `soup.a.string`: 标签内非属性字符串。
- `Comment`, `soup.html.string`: 标签内字符串的注释部分。

bs4标签节点遍历：
- 下行遍历：`.children`, `.contents`
- 上行遍历：`.parent`, `.parents`
- 平行遍历：`.next_sibling`, `.prev_sibling`

bs4中的`prettify()`方法。
```
soup.a.perttify()
```

> 查询
```python
soup.find_all('div')
```

## 信息标记

信息标记形式: `xml`, `json`, `yaml`

`xml`, 最早通用信息标记语言，可扩展好，但繁琐。
`json`, 信息有类型，适合程序处理，较简洁。
`yaml`, 信息无类型，文本信息比例最高，可读性好。各类系统的配置文件。

> yaml

```yaml
key1: val1
key2: val2
- value1
- value2
key3: 
    key4: val4
key5: # test
```

## scrapy

`scrapy`是一个爬虫框架，实现爬虫功能的一个软件结构和功能组件集合。

`scrapy`是5+2结构：
- EGINE 引擎
    整个框架的核心
    控制所有模块的数据流
    根据条件触发事件
    不需要用户修改
- SCHEDULER 调度器
    对所有爬虫请求进行调度管理
    不需要用户修改
- DOWLOADER 下载器
    根据请求下载网页
    不需要用户进行修改
- SPIDERS 爬虫
    解析`Dowloader`返回的响应(response)
    产生爬取项（scraped item）
    产生额外的爬取请求(request)
    需要用户编写配置代码
- ITEM PIPLINES 项目管道
    以流水线方式处理`Spiders`产生的爬取项
    由一组操作顺序组成，类似流水线，每个操作是一个`Item Piplines`类型。
    可能操作包括：清理，检验和查重爬取项中的HTML数据，将数据存储到数据库中。
    需要用户编写逻辑代码。

`Downloader Middlewares` 下载中间件：对`Engine`, `Scheduler`, `Downloader`之间进行用户可配置的控制。 用户可以根据该中间件，修改，丢弃，新增请求或响应。
`Spider Middlewares` 爬虫中间件：对`Spiders`和`Item Piplines`之间，对请求和爬取项的再处理。功能包括，修改，丢弃，新增请求或爬取项。

需要编写的模块：项目管道和爬虫，其它都是`scrapy`已经写好的。

```shell
scrapy startproject # 创建一个新项目
scrapy genspider # 创建一个爬虫
scrapy settings # 获得爬虫配置信息
scrapy crawl # 运行爬虫
scrapy list # 列出项目中所有爬虫
scrapy shell # 启动URL调试命令行
```
