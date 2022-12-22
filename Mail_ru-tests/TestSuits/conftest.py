from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest
import time
import os
from json import load as jsload
from logIO.logInOut import logIn


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="add browser name")
    parser.addoption("--language", action="store", default="en", help="add language")


@pytest.fixture(scope="class")
def oWebPage(request):
    browserName = request.config.getoption("browser_name")
    usedLanguage = request.config.getoption("language")

    url = r"https://mail.ru"
    if browserName == "chrome":
        options = ChromeOptions()
        options.add_experimental_option("prefs", {"intl.accept_languages": usedLanguage})
        sDriver = webdriver.Chrome(options=options)
    elif browserName == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", usedLanguage)
        sDriver = webdriver.Firefox(options=options)
    sDriver.maximize_window()
    sDriver.get(url)
    sDriver.implicitly_wait(3)
    yield sDriver
    print("\nEnding")
    time.sleep(3)
    sDriver.quit()


@pytest.fixture(scope="function")
def making_sure_loggedIn(oWebPage):
    try:
        vProfileButton = oWebPage.find_element(By.CSS_SELECTOR, "div[data-testid='whiteline-account']")
        assert vProfileButton
    except:
        with open(fr"{os.path.dirname(__file__)}\logIO\auth_data.json", "r") as vFile:
            diUserData = jsload(vFile)
        loginAuthOption = "valid"
        loginButtonOption = "main"
        oWebPage = logIn(oWebPage, diUserData, loginAuthOption, loginButtonOption)
    return oWebPage


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
