from selenium import webdriver

brower = webdriver.Chrome()
brower.get('https://www.taobao.com')
print(brower.page_source)
brower.close()