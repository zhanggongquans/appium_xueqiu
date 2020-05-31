import logging

import yaml
from appium.webdriver.webdriver import WebDriver

from page.wrapper import handle_black


class BasePage:
    '''
    定义基础类
    '''

    '''
    初始化 driver
    '''

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    '''
    公共配置在po里面封装
    '''

    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    def set_implicitly(self, time):
        self._driver.implicitly_wait(time)

    @handle_black
    def find(self, locator, value: str = None):
        element: WebDriver
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    def click(self, locator, value):
        return self._driver.find_element(locator, value).click()

    '''
    测试步骤的封装
    '''

    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            steps = yaml.safe_load(f)
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()
