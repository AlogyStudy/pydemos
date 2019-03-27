# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')

# print(response.read().decode('utf-8'))


import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'hello': 'world'}), encoding='utf-8')
res = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(res.read().decode('utf-8'))
