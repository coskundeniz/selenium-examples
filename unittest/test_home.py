import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_setup import get_webdriver_for

from pages.home import PythonDoctorHomePage


class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_webdriver_for("firefox")

    def setUp(self):
        self.pd_home_page = PythonDoctorHomePage(self.driver)

    def test_submit_question(self):

        code = """
def func():
print("Test function!")
        """
        question = "What is the output of the this code?"
        mail_address = "codenineeight@gmail.com"

        self.pd_home_page.enter_code(code)
        self.pd_home_page.enter_question(question)
        self.pd_home_page.enter_mail(mail_address)
        self.pd_home_page.submit_question()

        try:
            # wait for submit operation to complete
            wait = WebDriverWait(self.driver, timeout=5)
            submit_completed = wait.until(
                EC.presence_of_element_located(self.pd_home_page.SUBMIT_RESULT))

            if submit_completed:
                submit_info = self.driver.find_element(*self.pd_home_page.SUBMIT_RESULT)
                result_text = submit_info.text

                self.assertIn("Your question has been sent", result_text, "Submit Failed")

        except TimeoutException:
            self.driver.quit()

    def test_navigate_to_bopi_page(self):

        self.pd_home_page.navigate_to_bopi()

        self.assertEqual(self.driver.current_url, PythonDoctorHomePage.URL + "bopi/")

    def test_navigate_to_about(self):

        self.pd_home_page.navigate_to_about()

        self.assertEqual(self.driver.current_url, PythonDoctorHomePage.URL + "about/")

    def test_navigate_to_feedback(self):

        self.pd_home_page.navigate_to_feedback()

        self.assertEqual(self.driver.current_url, PythonDoctorHomePage.URL + "feedback/")

    def test_open_link(self):

        # store the ID of the original window
        original_window_handle = self.driver.current_window_handle

        self.pd_home_page.open_link(link_index=1)

        # wait for the new window/tab
        WebDriverWait(self.driver, timeout=5).until(EC.number_of_windows_to_be(2))

        # check if there are two windows/tabs
        self.assertEqual(len(self.driver.window_handles), 2)

        # switch back to original window
        self.driver.switch_to.window(original_window_handle)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":

    unittest.main()
