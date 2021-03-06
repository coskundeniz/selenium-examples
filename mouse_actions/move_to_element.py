from time import sleep
from selenium.webdriver import ActionChains
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")

driver.get("https://www.python.org/")

# locate the Downloads menu
downloads_menu = driver.find_element_by_id("downloads")

actions = ActionChains(driver)

# mouse over to Downloads menu
actions.move_to_element(downloads_menu).perform()

sleep(2)

driver.quit()
