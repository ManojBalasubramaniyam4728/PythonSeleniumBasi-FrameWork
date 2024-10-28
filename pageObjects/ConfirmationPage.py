from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class ConfirmationPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    countryTextField = (By.CSS_SELECTOR, "input[id='country']")
    checkBox = (By.XPATH, "//input[@id='checkbox2']/..//label")
    submitButton = (By.CSS_SELECTOR, "input[type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")

    def getCountryTextLocator(self, country_name):
        return (By.LINK_TEXT, country_name)

    def enterTheCountryAndClickOnIt(self, countryName, fullCountryName,waitTime):
        self.driver.find_element(*ConfirmationPage.countryTextField).send_keys(countryName)
        countryLocator = self.getCountryTextLocator(fullCountryName)
        self.waitUntilPresenceOfElementExplicitly(self.driver, waitTime, countryLocator)
        self.driver.find_element(*countryLocator).click()

    def clickOnTheCheckBox(self):
        self.driver.find_element(*ConfirmationPage.checkBox).click()

    def clickOnSubmitButton(self):
        self.driver.find_element(*ConfirmationPage.submitButton).click()

    def getTextFromSuccessMessage(self):
        return self.driver.find_element(*ConfirmationPage.successMessage).text