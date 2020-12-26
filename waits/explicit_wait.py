from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")
driver.get("https://www.pythondoctor.com")

try:
    # wait for typed text animation completed
    wait = WebDriverWait(driver, timeout=10)
    typing_completed = wait.until(EC.text_to_be_present_in_element((By.ID, "typed"),
                                                                    "fix your code..."))
    if typing_completed:
        element = driver.find_element_by_id("typed")
        print(f"Full text typed: {element.text}")

except TimeoutException:
    print("Timed out waiting for typing animation!")
finally:
    driver.quit()
