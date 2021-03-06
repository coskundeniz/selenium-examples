from time import sleep
from selenium.webdriver import ActionChains
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")

driver.get("https://crossbrowsertesting.github.io/drag-and-drop")

sleep(2)

source = driver.find_element_by_id("draggable")
target = driver.find_element_by_id("droppable")

target_x_offset = target.location.get("x")
target_y_offset = target.location.get("y")

actions = ActionChains(driver)
actions.drag_and_drop_by_offset(source, target_x_offset, target_y_offset / 3)
actions.perform()

sleep(3)

driver.quit()
