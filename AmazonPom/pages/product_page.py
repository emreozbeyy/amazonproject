from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ProductPage(BasePage):
    """ Add to wishlist """

    ADD_TO_LIST_BTN = (By.ID, "add-to-wishlist-button-submit")
    VIEW_YOUR_LIST_BUTTON = (By.LINK_TEXT, "View Your List")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)


    def add_to_list(self):
        """To close the page that appears after pressing the wishlist button """
        self.wait_for_element(self.ADD_TO_LIST_BTN).click()
        #self.wait_for_elements(self.CLOSE_BTN)[1].click()
        self.wait_for_element(self.VIEW_YOUR_LIST_BUTTON).click()
