import unittest
from selenium import webdriver
"""
测试账户:
用户名：user1  
密码：123456
"""

class Cnode(unittest.TestCase):

    def setUp(self):
        self.Url = 'http://39.107.96.138:3000/'
        self.driver = webdriver.Chrome()
        self.driver.get(self.Url)
        # 登陆用户
        self.driver.find_element_by_css_selector('a[href="/signin"]').click()
        # 用户名
        self.driver.find_element_by_id('name').send_keys('user1')
        # 密码
        self.driver.find_element_by_id('pass').send_keys('123456')
        # 登陆
        self.driver.find_element_by_css_selector('input[type="submit"]').click()
"""
登陆成功后,页面导航到首页
发布话题的操作
1.首页点击发布话题--话题发布页面
2.选择一个版块
3.输入标题
4.输入文本
5.提交

请将上述5步操作在下面test_post中实现
"""
    def test_post_topic(self):
        pass



    def tearDown(self):
        self.driver.save_screenshot('./posttopic.png')
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()






