import os
import time
from json import load as jsload

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expCond
from selenium.webdriver.support.ui import WebDriverWait


def logIn(oWebPage: webdriver, userData: dict, authOption: str, buttonOption: str) -> webdriver:

    diLoginButtonSelectors = {
        "main": "button[data-testid='enter-mail-primary']",
        "header": "div#ph-whiteline button.ph-login"
    }

    aAct = ActionChains(oWebPage)
    vLoginButton = oWebPage.find_element(By.CSS_SELECTOR, diLoginButtonSelectors[buttonOption])
    aAct.move_to_element(vLoginButton).pause(0.1).click().perform()
    time.sleep(1)
    # Switching to IFrame
    vLoginFrame = WebDriverWait(oWebPage, 5).until(expCond.presence_of_element_located(
                (By.CSS_SELECTOR, "iframe[src^='https://account.mail.ru/login/']")))
    oWebPage.switch_to.frame(vLoginFrame)
    time.sleep(1)

    vLogInField = WebDriverWait(oWebPage, 5).until(expCond.presence_of_element_located(
                (By.CSS_SELECTOR, "div#root form[method='POST'] input[name='username']")))
    vLogInField.send_keys(userData[authOption]["user"])

    vDomainSelector = oWebPage.find_element(By.CSS_SELECTOR, "div[data-test-id='domain-select']")
    vDomainSelector.click()
    time.sleep(0.1)
    vDomainPoint = oWebPage.find_element(By.CSS_SELECTOR, f"div#react-select-2-option-{userData[authOption]['domain']}")
    vDomainPoint.click()

    vSaveAuth = oWebPage.find_element(By.CSS_SELECTOR,
                                      "div.login-row div.submit-right-block>div.save-auth-field-wrap")
    autoAuthCheck = vSaveAuth.get_attribute("data-checked")
    if autoAuthCheck.lower() == "true":
        vSaveAuth.click()

    vNextButton = oWebPage.find_element(By.CSS_SELECTOR, "button[data-test-id='next-button']")
    vNextButton.click()
    time.sleep(0.1)

    vPassField = oWebPage.find_element(By.CSS_SELECTOR, "input[name='password']")
    vPassField.send_keys(userData[authOption]["pwd"])

    vSubmButton = oWebPage.find_element(By.CSS_SELECTOR, "button[data-test-id='submit-button']")
    vSubmButton.click()
    # switching back to entire web-page
    oWebPage.switch_to.default_content()
    return oWebPage


def logOutAdd(oWebPage) -> webdriver:
    actA = ActionChains(oWebPage)

    vProfileButton = oWebPage.find_element(By.CSS_SELECTOR, "div[data-testid='whiteline-account']")
    vProfileButton.click()
    time.sleep(0.1)
    vExitButton = oWebPage.find_element(By.CSS_SELECTOR, "div[data-testid='whiteline-account-exit']")
    vExitButton.click()
    return oWebPage


if __name__ == "__main__":
    def initWebDrv():
        url = r"https://mail.ru"
        vDriver = webdriver.Chrome()
        vDriver.maximize_window()
        vDriver.get(url)
        vDriver.implicitly_wait(5)
        return vDriver

    with open(fr"{os.path.dirname(__file__)}\auth_data.json", "r") as vFile:
        diUserData = jsload(vFile)
        loginAuthOption = "valid"
        loginButtonOption = "main"
    try:
        oDriver = initWebDrv()
        oDriver = logIn(oDriver, diUserData, loginAuthOption, loginButtonOption)
        oDriver = logOutAdd(oDriver)

    finally:
        time.sleep(10)
        oDriver.quit()
