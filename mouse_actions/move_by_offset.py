from time import sleep
from selenium.webdriver import ActionChains
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")

driver.get("https://www.python.org/")

# locate the Downloads menu
downloads_menu = driver.find_element_by_id("downloads")

actions = ActionChains(driver)

# mouse over to Downloads menu, and move below by yoffset 80px
actions.move_to_element(downloads_menu).pause(2)
actions.move_by_offset(xoffset=0, yoffset=80)
actions.perform()

sleep(3)

driver.quit()
