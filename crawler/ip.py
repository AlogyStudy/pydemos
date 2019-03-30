
'''
查询ip归属
'''
import requests


def main():
    inputval = input('请输入查询的要ip的地址：')
    url = 'http://m.ip138.com/ip.asp'
    kw = {
        'ip': inputval
    }
    res = requests.get(url, kw)
    print('查询的url地址为：', res.request.url)
    if res.status_code == 200:
        print(res.text)
    else:
        print(res.status_code)

if __name__ == '__main__':
    main()