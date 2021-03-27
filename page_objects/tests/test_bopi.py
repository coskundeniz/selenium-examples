from pages.bopi import BOPIPage


class TestBOPIPage:

    def __init__(self, driver):

        self.driver = driver
        self.pd_bopi_page = BOPIPage(self.driver)

    def test_best_practices_filter(self):

        self.pd_bopi_page.filter_best_practices_posts()

        assert self.driver.current_url == BOPIPage.URL + "filter/success/", "Invalid URL"

    def test_navigate_to_homepage(self):

        self.pd_bopi_page.navigate_to_homepage()

        assert self.driver.current_url == "https://www.pythondoctor.com/", "Invalid URL"
