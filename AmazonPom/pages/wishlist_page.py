from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.product_page import ProductPage
import time


class Wishlist(BasePage):
    """Delete the product in wishlist"""


    DELETE_BTN_2 = (By.NAME, "submit.deleteItem")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".a-size-base")
    WISHLIST_PRODUCT_NAME = (By.CSS_SELECTOR, ".a-size-base.a-link-normal")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def delete_wishlist(self):
        """To delete the product in wishlist and confirm that it has been deleted"""

        self.wait_for_element(self.DELETE_BTN_2).click()
        assert self.wait_for_element(self.PRODUCT_TITLE), "Product is not in wishlist"
        time.sleep(5)
