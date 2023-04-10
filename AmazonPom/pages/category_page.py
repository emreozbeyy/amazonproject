from selenium.webdriver.common.by import By
from base.base_page import BasePage



class CategoryPage(BasePage):
    """Select the third product from the category page"""

    NEXT_PAGE = (By.CLASS_NAME, "s-pagination-next")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".a-section.aok-relative.s-image-fixed-height")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, ".s-title-instructions-style .a-text-normal")
    SECOND_PAGE = (By.CLASS_NAME, "s-pagination-selected")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def next_page(self):
        assert self.wait_for_element(self.PRODUCT_DESCRIPTION).text.lower().find("samsung")>-1, "Samsung not found"
        #assert self.wait_for_element(self.PRODUCT_DESCRIPTION).text == '"samsung"', "Samsung not found"
        """Go to the second category page"""
        self.wait_for_element(self.NEXT_PAGE).click()
        assert self.wait_for_element(self.SECOND_PAGE).text == '2', "Not in second page"


    def select_third_product(self):
        """Choose the third product from the start"""
        self.wait_for_elements(self.PRODUCT_PAGE)[2].click()

