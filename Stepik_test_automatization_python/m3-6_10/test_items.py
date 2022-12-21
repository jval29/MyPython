# from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


@pytest.mark.usefixtures("browser")
class TestSuit01ItemPage:

    def test_01_button_AddItemToCart_present(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(url)
        time.sleep(1)
        try:
            addButton = browser.find_element(
                By.CSS_SELECTOR, "form#add_to_basket_form>input#id_quantity+button[type='submit']")
        except:
            addButton = None
        assert addButton, "Button 'Add to cart' not found"



