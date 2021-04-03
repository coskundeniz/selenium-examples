from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from components.navigation import Navigation


class BOPIPage:

    URL = "https://www.pythondoctor.com/bopi/"

    INFO_FILTER = (By.CLASS_NAME, "bg-info")
    BEST_FILTER = (By.CLASS_NAME, "bg-success")
    WARN_FILTER = (By.CLASS_NAME, "bg-danger")

    def __init__(self, driver):

        self.driver = driver
        self.navigation = Navigation(self.driver)

        self._load()

    def _load(self):

        self.driver.get(self.URL)

        try:
            # wait for all cards to load
            wait = WebDriverWait(self.driver, timeout=10)
            cards_loaded = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card")))

            assert len(cards_loaded) == 3

        except (AssertionError, TimeoutException):
            self.driver.quit()

    def filter_best_practices_posts(self):

        best_practices_link = self.driver.find_element(*self.BEST_FILTER)
        best_practices_link.click()

    def navigate_to_homepage(self):

        self.navigation.navigate_to_homepage()