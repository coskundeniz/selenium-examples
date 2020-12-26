from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from webdriver_setup import get_webdriver_for


class element_has_css_class():
    """Checks if given css class presents in the class attribute of the element"""

    def __init__(self, locator, css_class):
        self.locator = locator
        self.css_class = css_class

    def __call__(self, driver):

        try:
            element = driver.find_element(*self.locator)

            if element:
                return self.css_class in element.get_attribute("class")
            else:
                return False

        except StaleElementReferenceException:
            return False


driver = get_webdriver_for("firefox")
driver.get("https://www.pythondoctor.com")

try:
    # wait for typed text animation completed
    wait = WebDriverWait(driver, timeout=10)
    element_has_class = wait.until(element_has_css_class((By.ID, "typed"), "font-weight-light"))

    if element_has_class:
        print("Element has class looked for.")

except TimeoutException:
    print("Timed out waiting for typing animation!")
finally:
    driver.quit()
