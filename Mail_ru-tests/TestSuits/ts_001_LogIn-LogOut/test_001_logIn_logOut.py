# from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as expCond
import pytest
import os
# import time
# from lxml import objectify
from json import load
from logInOut import logIn


# getting auth-data from xml-file
# with open(fr"{os.path.dirname(__file__)}\auth_data.xml", "r") as vFile:
#     userData = objectify.fromstring(vFile.read())

# getting auth-data from json file
with open(fr"{os.path.dirname(__file__)}\auth_data.json", "r") as vFile:
    diUserData = load(vFile)


@pytest.mark.usefixtures("oWebPage")
class TestLogInLogOut:

    @pytest.mark.parametrize("loginButtonSelector", ["main", "header"])
    @pytest.mark.usefixtures("making_sure_loggedOut")
    def test_01_logIn_positive(self, oWebPage, loginButtonSelector):
        # loginButtonSelector = "main"
        oWebPage = logIn(oWebPage, diUserData, "valid", loginButtonSelector)
        try:
            userProfileButton = oWebPage.find_element(By.CSS_SELECTOR, "div[data-testid='whiteline-account']")
        except:
            userProfileButton = None
        assert userProfileButton, "User profile button not found"

    @pytest.mark.xfail(reason="Sometimes randomly redirects to logIn Frame otherwise than redirect to main page")
    @pytest.mark.usefixtures("making_sure_loggedIn", "logOut")
    def test_02_logOut(self, oWebPage):
        try:
            loginButton = oWebPage.find_element(By.CSS_SELECTOR, "button[data-testid='enter-mail-primary']")
        except:
            loginButton = None
        assert loginButton, "Login button not found"

    @pytest.mark.skip("test added to test_01 by parametrization")
    @pytest.mark.usefixtures("making_sure_loggedOut")
    def test_03_logIn_HeaderButton_positive(self, oWebPage):
        loginButtonSelector = "header"
        oWebPage = logIn(oWebPage, diUserData, "valid", loginButtonSelector)
        try:
            userProfileButton = oWebPage.find_element(By.CSS_SELECTOR, "div[data-testid='whiteline-account']")
        except:
            userProfileButton = None
        assert userProfileButton, "User profile button not found"

    @pytest.mark.negative
    @pytest.mark.usefixtures("making_sure_loggedOut")
    def test_04_logIn_mainButton_negative_WrongPassword_1(self, oWebPage):
        loginButtonSelector = "main"
        oWebPage = logIn(oWebPage, diUserData, "valid_userdomain_wrong_password_1", loginButtonSelector)
        time.sleep(1)
        try:
            vWrongPassMessage = oWebPage.find_element(By.CSS_SELECTOR, "div[data-test-id='password-input-error']")
        except:
            vWrongPassMessage = None
        assert vWrongPassMessage, "Error password message not found"


