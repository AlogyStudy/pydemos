
## 相关信息

- `robots.txt`协议，网络爬虫排除标准。

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

## Urllib

```python
# py2
import urllib2
res = urllib2.open('url')

# py3
import urllib.request
res = urllib.request.urlopen('url')
```
