from selenium.webdriver.common.by import By

from pageObjects.ProductListPage import ProductListPage


class HomePage:

    def __init__(self,driver):
        self.driver=driver

    shopLink=(By.PARTIAL_LINK_TEXT, "Shop")
    name=(By.NAME,"name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    gender = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    submit = (By.CSS_SELECTOR, "input[value='Submit']")
    success = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")


    def clickOnShopLink(self):
        self.driver.find_element(*HomePage.shopLink).click()
        return ProductListPage(self.driver)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.success)






