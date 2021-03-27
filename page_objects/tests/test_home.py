from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.home import PythonDoctorHomePage


class TestHomePage:

    def __init__(self, driver):

        self.driver = driver
        self.pd_home_page = PythonDoctorHomePage(self.driver)

    def test_navigate_to_bopi_page(self):

        self.pd_home_page.navigate_to_bopi()

        assert self.driver.current_url == PythonDoctorHomePage.URL + "bopi/"

    def test_navigate_to_about(self):

        self.pd_home_page.navigate_to_about()

        assert self.driver.current_url == PythonDoctorHomePage.URL + "about/"

    def test_navigate_to_feedback(self):

        self.pd_home_page.navigate_to_feedback()

        assert self.driver.current_url == PythonDoctorHomePage.URL + "feedback/"

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
                result_text = submit_info.text.split("\n")[0].strip()

                assert result_text == "Your question has been sent.", "Submit Failed"

        except TimeoutException:
            self.driver.quit()

    def test_open_link(self, link_index):

        self.pd_home_page.open_link(link_index)

        try:
            # wait for the new window/tab
            WebDriverWait(self.driver, timeout=5).until(EC.number_of_windows_to_be(2))

            # check if there are two windows/tabs
            assert len(self.driver.window_handles) == 2

        except TimeoutException:
            self.driver.quit()

