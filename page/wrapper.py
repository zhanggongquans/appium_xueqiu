import logging

from selenium.webdriver.common.by import By


def handle_black(func):

    print("into handle_black")

    def wrapper(*args, **kwargs):
        from page.base_page import BasePage
        _black_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']")
        ]
        _max_num = 3
        _error_num = 0
        instance: BasePage = args[0]
        try:
            element = func(*args, **kwargs)
            _error_num = 0
            return element
        except Exception as e:
            # 出现异常，将隐式等待设置最小，快速处理掉
            instance._driver.implicitly_wait(3)
            # 判断出现异常的次数
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in _black_list:
                elelist = instance.finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 隐式等待恢复成原来的
                    instance._driver.implicitly_wait(20)
                    return wrapper(*args, *kwargs)
            raise e
    return wrapper
