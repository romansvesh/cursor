from selenium.webdriver.common.by import By

__MENU_WITH_SUB_MENU = (By.XPATH, '//a[@href="#example-1-tab-2"]')
__SOME_MENU_WITH_SUB_MENU = (By.XPATH, '//li[@aria-haspopup="true"][1]')
__SUB_MENU = (By.XPATH, '//li[@aria-haspopup="true"][1]//ul')
__MENU_WITH_SUB_MENU_FRAME = (By.XPATH, '//div[@id = "example-1-tab-2"]//iframe')


def get_menu_with_sub_menu(driver):
    return driver.find_element(*__MENU_WITH_SUB_MENU)


def get_some_menu_with_sub_menu(driver):
    return driver.find_element(*__SOME_MENU_WITH_SUB_MENU)


def get_sub_menu(driver):
    return driver.find_element(*__SUB_MENU)


def get_menu_with_sub_menu_frame(driver):
    return driver.find_element(*__MENU_WITH_SUB_MENU_FRAME)