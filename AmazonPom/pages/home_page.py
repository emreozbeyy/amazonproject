from selenium.webdriver.common.by import By
from base.base_page import BasePage

class HomePage(BasePage):
    """Search from the search button"""

    search_name = "samsung"
    HOMEPAGE_CONTROL = (By.ID, "nav-logo-sprites")
    SEARCH_LOCATOR = (By.ID, "twotabsearchtextbox")
    SEARCH_CLICK_BTN = (By.ID, "nav-search-submit-button")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def search(self):
        """Search for word samsung"""
        assert self.wait_for_element(self.HOMEPAGE_CONTROL),"You are not at homepage!"
        self.wait_for_element(self.SEARCH_LOCATOR).send_keys(self.search_name)
        self.wait_for_element(self.SEARCH_CLICK_BTN).click()

