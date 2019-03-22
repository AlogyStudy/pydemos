
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
