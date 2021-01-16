from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from webdriver_setup import get_webdriver_for
from time import sleep


driver = get_webdriver_for("firefox")

driver.get("http://www.google.com")

search_input_box = driver.find_element(By.NAME, "q")

actions = ActionChains(driver)

actions.key_down(Keys.SHIFT)
actions.send_keys_to_element(search_input_box, "selenium")
actions.key_up(Keys.SHIFT)
actions.send_keys(" webdriver" + Keys.ENTER)
actions.perform()

sleep(5)

driver.quit()
