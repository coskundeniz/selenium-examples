import os
from time import sleep
from selenium.webdriver import ActionChains
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")

driver.get("http://jqueryui.com/droppable/")

sleep(2)

driver.switch_to.frame(0)

source = driver.find_element_by_id("draggable")
target = driver.find_element_by_id("droppable")

actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

sleep(3)

driver.quit()
