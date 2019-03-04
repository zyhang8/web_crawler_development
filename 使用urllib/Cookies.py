import http.cookiejar, urllib.request

# filename = 'cookiess.txt'
cookie = http.cookiejar.LWPCookieJar()
# cookie = http.cookiejar.LWPCookieJar(filename)
# cookie = http.cookiejar.MozillaCookieJar(filename)
# cookie = http.cookiejar.CookieJar()
cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
# cookie.save(ignore_discard=True, ignore_expires=True)

"""
for item in cookie:
    print(item.name+"="+item.value)
 """
