import requests
import json

# url = 'https://www.baidu.com/'
url = 'https://github.com/favicon.ico'

def getB():
    res = requests.get(url)
    # <class 'str'>
    # print(type(res.text), 'res')
    # # <class 'bytes'>
    # print(type(res.content), 'content')
    with open('f.ico', 'wb') as f:
        f.write(res.content)

def getC():
    files = {'file': open('./f.ico', 'rb')}
    res = requests.post('http://httpbin.org/post', files=files)
    print(res.text)

def getD():
    res = requests.get('http://httpbin.org/cookies')
    for key, value in res.cookies.items():
        print(key + '--' + value)

def getE():
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    response = s.get('http://httpbin.org/cookies')
    print(response.text)

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'

def main():
    # getB()
    # getC()
#     getD()
        # getE()
    ret = getHTMLText('http://www.baidu.com')
    print(ret)


if __name__ == '__main__':
    main()
