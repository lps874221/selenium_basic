from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

print(driver.title)

assert "google" not in driver.title

driver.find_element_by_id('kw').send_keys('Hello World')
driver.find_element_by_id('su').click()

time.sleep(2)

result = driver.find_element_by_id('content_left').text
print(result)

assert "Hello World" in result
