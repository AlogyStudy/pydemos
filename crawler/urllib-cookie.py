import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
resp = opener.open('http://www.baidu.com')

for item in cookie:
    print(item.name + '=' + item.value)
