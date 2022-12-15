from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


@pytest.fixture(scope="class")
def oWebPage():
    url = r"https://mail.ru"
    vDriver = webdriver.Chrome()
    vDriver.maximize_window()
    vDriver.get(url)
    vDriver.implicitly_wait(5)
    yield vDriver
    print("\nEnding")
    time.sleep(3)
    vDriver.quit()


def _logOut(oWebPage):
    vProfileButton = oWebPage.find_element(By.CSS_SELECTOR, "div[data-testid='whiteline-account']")
    vProfileButton.click()
    time.sleep(0.1)
    vExitButton = oWebPage.find_element(By.CSS_SELECTOR, "div[data-testid='whiteline-account-exit']")
    vExitButton.click()
    return oWebPage


@pytest.fixture(scope="function")
def logOut(oWebPage):
    return _logOut(oWebPage)


@pytest.fixture(scope="function")
def making_sure_loggedOut(oWebPage):
    try:
        vLoginButton = oWebPage.find_element(By.CSS_SELECTOR, "button[data-testid='enter-mail-primary']")
        assert vLoginButton
    except:
        url = r"https://mail.ru"
        oWebPage.get(url)
        return _logOut(oWebPage)
