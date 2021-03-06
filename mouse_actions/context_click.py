from time import sleep
from selenium.webdriver import ActionChains
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")

driver.get("https://www.python.org/")

search_bar = driver.find_element_by_name("q")

actions = ActionChains(driver)
actions.context_click(search_bar).perform()

sleep(2)

driver.quit()
