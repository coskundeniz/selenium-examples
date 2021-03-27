from selenium.webdriver.common.by import By


class Navigation:

    ABOUT_PAGE_LOCATOR    = (By.LINK_TEXT, "About")
    BOPI_PAGE_LOCATOR     = (By.LINK_TEXT, "BOPI")
    FEEDBACK_PAGE_LOCATOR = (By.LINK_TEXT, "Feedback")
    HOME_PAGE_LOCATOR     = (By.LINK_TEXT, "Python Doctor")

    def __init__(self, driver):

        self.driver = driver

    def navigate_to_homepage(self):

        homepage_link = self.driver.find_element(*self.HOME_PAGE_LOCATOR)
        homepage_link.click()

    def navigate_to_about(self):

        about_page_link = self.driver.find_element(*self.ABOUT_PAGE_LOCATOR)
        about_page_link.click()

    def navigate_to_bopi_page(self):

        bopi_page_link = self.driver.find_element(*self.BOPI_PAGE_LOCATOR)
        bopi_page_link.click()

    def navigate_to_feedback(self):

        feedback_page_link = self.driver.find_element(*self.FEEDBACK_PAGE_LOCATOR)
        feedback_page_link.click()
