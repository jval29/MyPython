from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions
import time
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="add browser name")
    parser.addoption("--language", action="store", default="en", help="add language")


@pytest.fixture(scope="class")
def browser(request):  # collecting initial options for selenium driver(browser)
    browserName = request.config.getoption("browser_name").lower().strip()
    userLanguage = request.config.getoption("language").lower().strip()

    if browserName == "chrome":
        options = chromeOptions()
        options.add_experimental_option("prefs", {"intl.accept_languages": userLanguage})
        sDriver = webdriver.Chrome(options=options)
    elif browserName == "firefox":
        options = firefoxOptions()
        options.set_preference("intl.accept_languages", userLanguage)
        sDriver = webdriver.Firefox(options=options)

    sDriver.maximize_window()
    sDriver.implicitly_wait(5)
    yield sDriver

    time.sleep(5)
    print("Tests ending")
    sDriver.quit()

