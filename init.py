
import unittest
from selenium import webdriver

class InitTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.shiguangkey.com')
    def tearDown(self):
        self.driver.quit()
