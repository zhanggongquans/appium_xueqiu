from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    _activity = ".view.WelcomeActivityAlias"
    _package = "com.xueqiu.android"

    '''
    封装app应用的入口函数
    进行driver是否存在进行判断
    '''

    def start(self):
        if self._driver is None:
            cap = dict()
            cap["platformName"] = "android"
            cap["deviceName"] = "127.0.0.1:7555"
            cap["platformVersion"] = "6.0"
            cap["appPackage"] = self._package
            cap["appActivity"] = self._activity
            cap["noReset"] = "true"
            cap["unicodeKeyboard"] = "true"
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
            self._driver.implicitly_wait(20)
        else:
            self._driver.start_activity(self._activity, self._package)

        return self

    '''
    进入到main方法中进行操作
    return实现语法糖的效果
    '''

    def main(self) -> Main:
        return Main(self._driver)
