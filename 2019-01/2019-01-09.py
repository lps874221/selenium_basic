

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://s.weibo.com/')

driver.find_element_by_css_selector('div[class="search-input"] > input[type="text"]').send_keys('web自动化')
driver.find_element_by_css_selector('.s-btn-b').click()


driver.find_element_by_link_text('高级搜索').click()
driver.find_element_by_css_selector('label[for="radio03"]').click()

driver.find_element_by_link_text('搜索微博').click()


eles = driver.find_elements_by_css_selector('div[action-type="feed_list_item"]')


# todo 找到每个微博中的 标题，发送人，发布时间，来源，收藏数，转发数，评论数，点赞数

