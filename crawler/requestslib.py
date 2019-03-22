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

def main():
    # getB()
    # getC()
    getD()


if __name__ == '__main__':
    main()
