import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BaiDuSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')

    def test_link_text(self):
        driver= self.driver
        driver.find_element_by_link_text("新闻").click()
     
    def test_Partial_link_text(self):
        driver = self.driver
        driver.find_element_by_partial_link_text('新').click()
    
    # TODO
    def test_class_name(self):
        driver = self.driver
        driver.find_element_by_class_name('s_ipt').send_keys('className')
    
    

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()