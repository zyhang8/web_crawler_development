from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_elements_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
lis = browser.find_elements_by_css_selector('.service-bd li')
print(input_first, input_second, input_third)
print(lis)
browser.close()