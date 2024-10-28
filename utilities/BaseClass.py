import logging

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("setup")
class BaseClass:

    def scrollTillElementIsVisibleFromActionChain(self, driver, element):
        action = ActionChains(driver)
        action.scroll_to_element(element).perform()

    def waitUntilPresenceOfElementExplicitly(self, driver, explicitlyTime, locator):
        wait = WebDriverWait(driver, explicitlyTime)
        wait.until(EC.presence_of_element_located(locator))

    def selectByText(self,element,text):
        select=Select(element)
        select.select_by_visible_text(text)

    def getLogger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('C:/Users/manoj.b/PycharmProjects/PythonSelfFramework/reports/logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger