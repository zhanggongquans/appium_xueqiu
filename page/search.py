from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Search(BasePage):
    def search(self, name):
        self.find(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]').send_keys("alibaba")
        self.find(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/name"]').click()
        self.find(By.XPATH,
                  f'//*[contains(@resource-id,"ll_stock_item_container")]//*[@text="{name}"]/../..//*[@text = "加自选"]').click()

    def is_choose(self, name):
        eles = self.finds(By.XPATH,
                          f'//*[contains(@resource-id,"ll_stock_item_container")]//*[@text="{name}"]/../..//*[@text = "已添加"]')
        return len(eles) > 0
