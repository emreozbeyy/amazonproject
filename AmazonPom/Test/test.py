from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from pages.wishlist_page import Wishlist
import unittest


class TestAmazon(unittest.TestCase):
    """Test case is:
    1. Go to website
    2. Click login page button
    3. Try to logged in
    4. Search "samsung" on site
    5. Search third product result of search
    6. Add product to wishlist
    7. Go to wishlist
    8. Delete items from wishlist
    9. Tear down
    """

    def setUp(self):
        self.website = "https://www.amazon.com/"
        self.driver = webdriver.Chrome("C:/Users/emre.ozbey/Desktop/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.LoginPage = LoginPage(self.driver)
        self.HomePage = HomePage(self.driver)
        self.CategoryPage = CategoryPage(self.driver)
        self.ProductPage = ProductPage(self.driver)
        self.Wishlist = Wishlist(self.driver)

    def test_amazon(self):
        self.LoginPage.login()
        self.HomePage.search()
        self.CategoryPage.next_page()
        self.CategoryPage.select_third_product()
        self.ProductPage.add_to_list()
        self.Wishlist.delete_wishlist()

    def TearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
