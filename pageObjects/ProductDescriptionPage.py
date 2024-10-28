from selenium.webdriver.common.by import By

from pageObjects.ConfirmationPage import ConfirmationPage


class ProductDescriptionPage:

    def __init__(self,driver):
        self.driver=driver

    checkoutButton=(By.XPATH, "//button[@class='btn btn-success']")

    def clickOnCheckoutButton(self):
        self.driver.find_element(*ProductDescriptionPage.checkoutButton).click()
        return ConfirmationPage(self.driver)
