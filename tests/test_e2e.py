from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log=self.getLogger()
        log.info("Successfully opened browser and maximized browser window navigate to application url")
        expectedProductName = "Blackberry"
        homePage=HomePage(self.driver)
        productListPages=homePage.clickOnShopLink()
        log.info("Successfully Clicked On The Shop Link And Navigated to Shop Page")
        productListItems = productListPages.getNumberOfProducts()
        log.info("Successfully fetched number of product and navigated to Product List Page")
        productListPages.addTheItemToTheCart(productListItems,expectedProductName)
        log.info("Successfully added "+expectedProductName+" Product To cart")
        self.scrollTillElementIsVisibleFromActionChain(self.driver,productListPages.checkoutButtonElement())
        log.info("Successfully scrolled till check out button")
        productDescriptionPage=productListPages.clickOnCheckOutButton()
        log.info("Successfully Clicked On check out button And Navigated to Product Description Page")
        confirmationPage=productDescriptionPage.clickOnCheckoutButton()
        log.info("Successfully Clicked On check out button And Navigated to Confirmation Page")
        confirmationPage.enterTheCountryAndClickOnIt("Ind","India",10)
        log.info("Successfully Entered 'Ind' in country text field and waited for India to select")
        confirmationPage.clickOnTheCheckBox()
        log.info("Successfully Clicked On CheckBox")
        confirmationPage.clickOnSubmitButton()
        log.info("Successfully Clicked On The submit button")
        alertMessage = confirmationPage.getTextFromSuccessMessage()
        log.info("Successfully fetched The success message and message is "+alertMessage)
        assert "Success! Thank" in alertMessage
        log.info("Success! Thank"+" is present in "+ alertMessage)

