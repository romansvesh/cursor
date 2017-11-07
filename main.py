import unittest

import time
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import visibility_of
from helpers import helper
from page import menu_page


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('lib\chromedriver.exe')

    def test_clipboard_copy_by_button(self):
        self.driver.get("http://way2automation.com/way2auto_jquery/menu.php")
        helper.login(self.driver)
        self.driver.get("http://way2automation.com/way2auto_jquery/menu.php")
        time.sleep(5)
        #helper.open_some_menu_with_submenu(self.driver)

        self.assertTrue(visibility_of(
            menu_page.get_sub_menu(self.driver)))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
