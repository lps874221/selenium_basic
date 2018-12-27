import unittest
from selenium import webdriver
"""
测试账户:
用户名：testuser01  
密码：123456
"""

class Cnode(unittest.TestCase):

    def setUp(self):
        self.Url = 'http://39.107.96.138:3000/'
        self.driver = webdriver.Chrome()
        self.driver.get(self.Url)

    def test_register(self):
        driver = self.driver
        driver.find_element_by_css_selector('a[href="/signup"]').click()
        driver.find_element_by_id('loginname').send_keys('xiaoming')
        driver.find_element_by_id('pass').send_keys('xxxxxx')
        driver.find_element_by_id('re_pass').send_keys('xxxxxx')
        driver.find_element_by_id('email').send_keys('xxxxx')
        driver.find_element_by_css_selector('input[type="submit"]').click()   

    def test_login(self):
        pass


    def tearDown(self):
        self.driver.save_screenshot('./01.png')
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()






