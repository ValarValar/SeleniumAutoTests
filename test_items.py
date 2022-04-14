import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
from selenium.webdriver.common.by import By

class TestItems():

    @pytest.mark.smoke
    def test_item_has_add_to_basket_button(self, browser):
        browser.get(link)
        button = browser.find_elements(by=By.CSS_SELECTOR, value="#add_to_basket_form button.btn-add-to-basket")
        assert button, "Кнопка не была найдена!"