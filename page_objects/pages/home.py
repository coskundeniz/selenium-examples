from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from components.navigation import Navigation
from components.links import Links


class PythonDoctorHomePage:

    URL = "https://www.pythondoctor.com/"

    CODE_INPUT     = (By.CLASS_NAME, "ace_text-input")
    QUESTION_INPUT = (By.ID, "id_question_text")
    MAIL_INPUT     = (By.ID, "id_questioner")
    SUBMIT_BUTTON  = (By.NAME, "submit")
    SUBMIT_RESULT  = (By.CLASS_NAME, "alert")

    def __init__(self, driver):

        self.driver = driver
        self.navigation = Navigation(self.driver)
        self.links = Links(self.driver)

        self._load()

    def _load(self):

        self.driver.get(self.URL)

        try:
            # wait for typed text animation completed
            wait = WebDriverWait(self.driver, timeout=10)
            typing_completed = wait.until(EC.text_to_be_present_in_element((By.ID, "typed"),
                                                                            "fix your code..."))
        except TimeoutException:
            print("Timed out waiting for typing animation!")
            self.driver.quit()

    def enter_code(self, code_text):

        code_input_area = self.driver.find_element(*self.CODE_INPUT)
        code_input_area.send_keys(code_text)

    def enter_question(self, question_text):

        question_input_area = self.driver.find_element(*self.QUESTION_INPUT)
        question_input_area.send_keys(question_text)

    def enter_mail(self, mail_address):

        mail_input_area = self.driver.find_element(*self.MAIL_INPUT)
        mail_input_area.send_keys(mail_address)

    def submit_question(self):

        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON)
        submit_button.click()

    def navigate_to_bopi(self):

        self.navigation.navigate_to_bopi_page()

    def navigate_to_about(self):

        self.navigation.navigate_to_about()

    def navigate_to_feedback(self):

        self.navigation.navigate_to_feedback()

    def open_link(self, link_index):

        self.links.open_link(link_index)

