#coding:utf-8
import unittest
from init import  InitTest

class Login(InitTest):
    def test_login(self):
        # self.assertEqual(self.driver.current_url, 'https://www.shiguangkey.com/')
        self.driver.get('https://www.shiguangkey.com/')
        self.driver.find_element_by_css_selector('#__layout > div > div > header > div > div > div.userinfo-contianer > div.userinfo__unlogin > span:nth-child(1)').click()
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_css_selector('#accountLogin').click()
        self.driver.find_element_by_css_selector('#loginAccount').send_keys('t0327627844')
        self.driver.find_element_by_css_selector('#password').send_keys('123456a')
        self.driver.find_element_by_css_selector('loginButton___1GO7F').submit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

