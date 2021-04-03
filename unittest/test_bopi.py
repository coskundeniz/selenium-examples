import unittest
from webdriver_setup import get_webdriver_for

from pages.bopi import BOPIPage


class TestBOPIPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_webdriver_for("firefox")

    def setUp(self):
        self.pd_bopi_page = BOPIPage(self.driver)

    def test_best_practices_filter(self):

        self.pd_bopi_page.filter_best_practices_posts()

        self.assertEqual(self.driver.current_url, BOPIPage.URL + "filter/success/")

    def test_navigate_to_homepage(self):

        self.pd_bopi_page.navigate_to_homepage()

        self.assertEqual(self.driver.current_url, "https://www.pythondoctor.com/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":

    unittest.main()
