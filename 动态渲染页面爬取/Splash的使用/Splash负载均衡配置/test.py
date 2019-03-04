import requests
from urllib.parse import quote
import re

lua = '''
fuction main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://httpbin.org/get")
    return treat.as_string(response.body)
end
'''

url = 'http://splash:8050/execute?Lua_source=' + quote(lua)
response = requests.get(url, auth=('admin', 'admin'))
ip = re.search('(\d+\.\d+\.\d+\.\d+)',response.text).group(1)
print(ip)