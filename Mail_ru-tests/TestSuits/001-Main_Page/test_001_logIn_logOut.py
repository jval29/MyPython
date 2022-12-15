
import time
from selenium.webdriver.common.by import By
import pytest
import os
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

    @pytest.mark.usefixtures("making_sure_loggedOut")
    def test_01_logIn_mainButton_positive(self, oWebPage):
        loginButtonSelector = "main"
        oWebPage = logIn(oWebPage, diUserData, "valid", loginButtonSelector)
        userProfileButton = None
        try:
            userProfileButton = oWebPage.find_element(By.CSS_SELECTOR, "div[data-testid='whiteline-account']")
        finally:
            assert userProfileButton, "User profile button not found"

    @pytest.mark.xfail(reason="Sometimes randomly redirects to logIn Frame")
    @pytest.mark.usefixtures("logOut")
    def test_02_logOut(self, oWebPage):
        loginButton = None
        try:
            loginButton = oWebPage.find_element(By.CSS_SELECTOR, "button[data-testid='enter-mail-primary']")
        finally:
            assert loginButton, "Login button not found"

    @pytest.mark.usefixtures("making_sure_loggedOut")
    def test_03_logIn_HeaderButton_positive(self, oWebPage):
        loginButtonSelector = "header"
        oWebPage = logIn(oWebPage, diUserData, "valid", loginButtonSelector)
        userProfileButton = None
        try:
            userProfileButton = oWebPage.find_element(By.CSS_SELECTOR, "div[data-testid='whiteline-account']")
        finally:
            assert userProfileButton, "User profile button not found"

    @pytest.mark.negative
    @pytest.mark.usefixtures("making_sure_loggedOut")
    def test_04_logIn_mainButton_negative_WrongPassword_1(self, oWebPage):
        loginButtonSelector = "main"
        oWebPage = logIn(oWebPage, diUserData, "valid_userdomain_wrong_password_1", loginButtonSelector)
        time.sleep(1)
        vWrongPassMessage = None
        try:
            vWrongPassMessage = oWebPage.find_element(By.CSS_SELECTOR, "div[data-test-id='password-input-error']")
        finally:
            assert vWrongPassMessage, "Error password message not found"
            
