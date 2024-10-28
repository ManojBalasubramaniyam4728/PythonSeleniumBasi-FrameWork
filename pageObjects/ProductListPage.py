from selenium.webdriver.common.by import By

from pageObjects.ProductDescriptionPage import ProductDescriptionPage


class ProductListPage:

    def __init__(self,driver):
        self.driver=driver

    productListItems=(By.XPATH, "//div[@class='card h-100']")
    actualProductName = (By.XPATH, "div/h4/a")
    addToCartButton=(By.XPATH, "div/button[@class='btn btn-info']")
    checkoutButton=(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")

    def getNumberOfProducts(self):
        return self.driver.find_elements(*ProductListPage.productListItems)

    def checkoutButtonElement(self):
        return self.driver.find_element(*ProductListPage.checkoutButton)

    def addTheItemToTheCart(self,productListItems,expectedProductName):
        for productListItem in productListItems:
            actualProductName = productListItem.find_element(*ProductListPage.actualProductName).text
            if actualProductName == expectedProductName:
                productListItem.find_element(*ProductListPage.addToCartButton).click()

    def clickOnCheckOutButton(self):
         self.driver.find_element(*ProductListPage.checkoutButton).click()
         return ProductDescriptionPage(self.driver)



