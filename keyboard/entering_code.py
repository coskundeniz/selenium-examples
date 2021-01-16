from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_setup import get_webdriver_for
from time import sleep


driver = get_webdriver_for("firefox")

driver.get("https://www.pythondoctor.com")

try:
    # wait for typed text animation completed to cursor focus on textarea
    wait = WebDriverWait(driver, timeout=10)
    typing_completed = wait.until(EC.text_to_be_present_in_element((By.ID, "typed"), "fix your code..."))
except TimeoutException:
    print("Timed out waiting for typing animation!")
    driver.quit()

if typing_completed:
    code_area = driver.find_element_by_class_name("ace_text-input")
    code_area.send_keys("def foo():" + Keys.ENTER)
    sleep(1)
    code_area.send_keys("pass")

    sleep(2)

    ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()

    sleep(3)

driver.quit()
