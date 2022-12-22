#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expCond
import pytest
import time


@pytest.mark.usefixtures("oWebPage")
class TestWriteLetter:

    @pytest.mark.smoke
    @pytest.mark.usefixtures("making_sure_loggedIn")
    def test_01_letter_form_opens(self, oWebPage):
        time.sleep(0.1)
        aActions = ActionChains(oWebPage)
        try:  # closing random-appearing Promo-window
            vPromoWindow = oWebPage.find_element(By.CSS_SELECTOR, "div.ph-project-promo-container>a[data-show-pixel]")
            vPromoWindowCloseButton = oWebPage.find_element(
                            By.CSS_SELECTOR, "div.ph-project-promo-container>a svg.ph-project-promo-close-icon__svg")
            aActions.move_to_element(vPromoWindowCloseButton).pause(0.1).click().perform()
        finally:
            time.sleep(0.1)
        vLetterCreateButton = oWebPage.find_element(By.CSS_SELECTOR, "a[href='/compose/'].compose-button")
        vLetterCreateButton.click()

        vMailForm = None
        try:
            vMailForm = WebDriverWait(oWebPage, 3).until(expCond.presence_of_element_located((
                By.CSS_SELECTOR, "div.focus-zone.focus-zone_fluid")))
        finally:
            assert vMailForm, "Web-Form to write the letter not found"

    @pytest.mark.usefixtures("making_sure_loggedIn")
    def test_02_letter_form_closes_with_close_button(self, oWebPage):
        time.sleep(0.1)
        try:  # check for Form is open
            vMailForm = WebDriverWait(oWebPage, 1).until(expCond.presence_of_element_located(
                                        (By.CSS_SELECTOR, "div.focus-zone.focus-zone_fluid")))
            assert vMailForm
        except:  # trying to open Form if it isn't present
            vLetterCreateButton = oWebPage.find_element(By.CSS_SELECTOR, "a[href='/compose/'].compose-button")
            vLetterCreateButton.click()

        vFormCloseButton = oWebPage.find_element(
                    By.CSS_SELECTOR, "div.focus-zone.focus-zone_fluid div.container--8PdPf>div>button:last-child svg")
        vFormCloseButton.click()
        time.sleep(1)
        try:
            vMailForm = oWebPage.find_element(By.CSS_SELECTOR, "div.focus-zone.focus-zone_fluid")
        except:
            vMailForm = None
        finally:
            assert not vMailForm
