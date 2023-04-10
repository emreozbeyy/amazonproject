from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage (BasePage):
    """Do login process in login page"""

    Mail = "emre33ozbey.com@gmail.com"
    password = "741852Aa."

    LOGIN_BTN = (By.ID, "nav-link-accountList-nav-line-1")
    EMAIL_LOCATOR = (By.ID, "ap_email")
    CONTINUE_BTN = (By.CSS_SELECTOR, "#continue")
    PASSWORD_LOCATOR = (By.ID, "ap_password")
    SIGN_BTN = (By.ID, "signInSubmit")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def login(self):
        """Enter your mail and password and login in """
        self.wait_for_element(self.LOGIN_BTN).click()
        self.wait_for_element(self.EMAIL_LOCATOR).send_keys(self.Mail)
        self.wait_for_elements(self.CONTINUE_BTN)[1].click()
        self.wait_for_element(self.PASSWORD_LOCATOR).send_keys(self.password)
        self.wait_for_element(self.SIGN_BTN).click()
