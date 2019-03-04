from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener


proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1'
})
opener = build_opener(proxy_handler)

response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))
