
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.get('http://39.107.96.138:3000/signin')

driver.find_element_by_xpath('//*[@id="name"]').send_keys('user1')
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('123456')
driver.find_element_by_xpath('//*[@type="submit"]').click()

driver.find_element_by_xpath('//*[@id="create_topic_btn"]').click()

driver.find_element_by_xpath('//*[@id="tab-value"]').click()
driver.find_element_by_xpath('//*[@id="tab-value"]/option[2]').click()

driver.find_element_by_xpath('//*[@id="title"]').send_keys('helloworld')

content_area = driver.find_element_by_xpath('//*[@class="CodeMirror-scroll"]')
content_area.click()

actions = ActionChains(driver)
actions.move_to_element(content_area)
actions.send_keys("abc")

# TODO 在文本输入里面模拟快捷键 Ctrl + b 操作


actions.perform()