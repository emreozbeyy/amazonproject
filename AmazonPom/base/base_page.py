from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage(object):
    """Base class to initialize the base page that will bw called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def wait_for_element(self, locator):
        """wait the element until clickable"""
        return self.wait.until(ec.element_to_be_clickable(locator))

    def wait_for_elements(self, locator):
        """wait the elements until clickable"""
        return self.wait.until(ec.presence_of_all_elements_located(locator))

    def hover(self, locator):
        """hover the given locator"""
        hover_element = self.wait_for_element(locator)
        hover = ActionChains(self.driver).move_to_element(hover_element)
        hover.perform()

    def wait_element_visible(self, element):
        """
        Wait for element to visible
        """
        return self.wait.until(ec.visibility_of_element_located(element))
