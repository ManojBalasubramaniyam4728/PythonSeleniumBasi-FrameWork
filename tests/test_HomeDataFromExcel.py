import pytest

from pageObjects.HomePage import HomePage
from testData.ExcelDataUtilities import ExcelUtilities
from utilities.BaseClass import BaseClass


class TestData(BaseClass):

    def test_verifyFormFillingWithTestDataFromExcel(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstName"])
        log.info("Successfully Entered The '" + getData["firstName"] + "' in name Text field")
        homepage.getEmail().send_keys(getData["email"])
        log.info("Successfully Entered The '" + getData["email"] + "' in email id Text field")
        homepage.getPassword().send_keys(getData["password"])
        log.info( "Successfully Entered The '" + getData["password"] + "' in password Text field")
        self.selectByText(homepage.getGender(), getData["gender"])
        log.info("Successfully selected The '" + getData["gender"] + "' From Gender dropdown")
        homepage.getSubmit().click()
        log.info("Successfully clicked on submit button")
        message = homepage.getSuccessMessage().text.strip()
        log.info("Successfully fetched " + message)
        assert "The Form has been submitted successfully!." in message
        log.info("The Form has been submitted successfully!" + " is present in " + message)
        self.driver.refresh()
        log.info("Successfully refreshed the browser window")

    @pytest.fixture(params=ExcelUtilities.getTestData("User1"))
    def getData(self, request):
        return request.param