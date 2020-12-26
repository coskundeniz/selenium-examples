from webdriver_setup import get_webdriver_for
from selenium.common.exceptions import NoSuchElementException


driver = get_webdriver_for("firefox")
# set waiting to 10 seconds
driver.implicitly_wait(10)
driver.get("https://www.pythondoctor.com")

try:
    # the correct id is "typed
    element = driver.find_element_by_id("typer")
    print(f"Full text typed: {element.text}")
except NoSuchElementException as e:
    print(e)
finally:
    driver.quit()

