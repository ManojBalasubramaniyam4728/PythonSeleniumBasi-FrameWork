import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHome(BaseClass):

    def test_verifyFormFillingWithHardCode(self):
        log = self.getLogger()
        log.info("Successfully opened browser and maximized browser window navigate to application url")
        homepage=HomePage(self.driver)
        homepage.getName().send_keys("Dada")
        log.info("Successfully Entered The 'Data' in name Text field")
        homepage.getEmail().send_keys("dada123@gmail.com")
        log.info("Successfully Entered The 'dada123@gmail.com' in email id Text field")
        homepage.getPassword().send_keys("Password@123")
        log.info("Successfully Entered The 'Password@123' in password Text field")
        self.selectByText(homepage.getGender(),"Male")
        log.info("Successfully selected male in gender dropdown")
        homepage.getSubmit().click()
        log.info("Successfully Clicked on Submit button")
        message=homepage.getSuccessMessage().text.strip()
        log.info("Successfully fetched "+message)
        assert "The Form has been submitted successfully!." in message
        log.info("The Form has been submitted successfully!"+" is present in "+ message)
        self.driver.refresh()
        log.info("Successfully refreshed the browser window")

    def test_verifyFormFillingWithTuple(self,getDataInListAndTuple):
        log = self.getLogger()
        homepage=HomePage(self.driver)
        homepage.getName().send_keys(getDataInListAndTuple[0])
        log.info("Successfully Entered The '"+getDataInListAndTuple[0]+"' in name Text field")
        homepage.getEmail().send_keys(getDataInListAndTuple[1])
        log.info("Successfully Entered The '"+getDataInListAndTuple[1]+"' in email id Text field")
        homepage.getPassword().send_keys(getDataInListAndTuple[2])
        log.info("Successfully Entered The '"+getDataInListAndTuple[2]+"' in password Text field")
        self.selectByText(homepage.getGender(),getDataInListAndTuple[3])
        log.info("Successfully selected The '"+getDataInListAndTuple[3]+"' From Gender dropdown")
        homepage.getSubmit().click()
        log.info("Successfully clicked on submit button")
        message=homepage.getSuccessMessage().text.strip()
        log.info("Successfully fetched "+message)
        assert "The Form has been submitted successfully!." in message
        log.info("The Form has been submitted successfully!" + " is present in " + message)
        self.driver.refresh()
        log.info("Successfully refreshed the browser window")


    def test_verifyFormFillingWithDictionary(self,getDataInDictionary):
        log = self.getLogger()
        homepage=HomePage(self.driver)
        homepage.getName().send_keys(getDataInDictionary["firstName"])
        log.info("Successfully Entered The '" + getDataInDictionary["firstName"] + "' in name Text field")
        homepage.getEmail().send_keys(getDataInDictionary["email"])
        log.info("Successfully Entered The '" + getDataInDictionary["email"] + "' in email id Text field")
        homepage.getPassword().send_keys(getDataInDictionary["password"])
        log.info("Successfully Entered The '" + getDataInDictionary["password"] + "' in password Text field")
        self.selectByText(homepage.getGender(),getDataInDictionary["gender"])
        log.info("Successfully selected The '" + getDataInDictionary["gender"] + "' From Gender dropdown")
        homepage.getSubmit().click()
        log.info("Successfully clicked on submit button")
        message=homepage.getSuccessMessage().text.strip()
        log.info("Successfully fetched " + message)
        assert "The Form has been submitted successfully!." in message
        log.info("The Form has been submitted successfully!" + " is present in " + message)
        self.driver.refresh()
        log.info("Successfully refreshed the browser window")

    def test_verifyFormFillingWithDictionaryFromAnotherFile(self, getDataInDictionaryFromAnotherFile):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getDataInDictionaryFromAnotherFile["firstName"])
        log.info("Successfully Entered The '" + getDataInDictionaryFromAnotherFile["firstName"] + "' in name Text field")
        homepage.getEmail().send_keys(getDataInDictionaryFromAnotherFile["email"])
        log.info("Successfully Entered The '" + getDataInDictionaryFromAnotherFile["email"] + "' in email id Text field")
        homepage.getPassword().send_keys(getDataInDictionaryFromAnotherFile["password"])
        log.info("Successfully Entered The '" + getDataInDictionaryFromAnotherFile["password"] + "' in password Text field")
        self.selectByText(homepage.getGender(), getDataInDictionaryFromAnotherFile["gender"])
        log.info("Successfully selected The '" + getDataInDictionaryFromAnotherFile["gender"] + "' From Gender dropdown")
        homepage.getSubmit().click()
        log.info("Successfully clicked on submit button")
        message = homepage.getSuccessMessage().text.strip()
        log.info("Successfully fetched " + message)
        assert "The Form has been submitted successfully!." in message
        log.info("The Form has been submitted successfully!" + " is present in " + message)
        self.driver.refresh()
        log.info("Successfully refreshed the browser window")

    @pytest.fixture(params=[("Manoj","manojbalasubramaniyam4488@gmail.com","Password@123","Male"),("Sanjay","sanjay123@gmail.com","Sanjay@123","Male")])
    def getDataInListAndTuple(self,request):
        return request.param

    @pytest.fixture(params=[
        {"firstName": "Manoj", "email": "manojbalasubramaniyam4488@gmail.com", "password": "password@123","gender": "Male"},
        {"firstName": "Sanjay", "email": "sanjay123@gmail.com", "password": "Sanjay@123", "gender": "Male"}])
    def getDataInDictionary(self, request):
        return request.param

    @pytest.fixture(params=HomePageData.test_HomePageDictionary)
    def getDataInDictionaryFromAnotherFile(self, request):
        return request.param
