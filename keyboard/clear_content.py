from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_setup import get_webdriver_for
from time import sleep


driver = get_webdriver_for("firefox")

driver.get("http://www.google.com")

search_input_box = driver.find_element(By.NAME, "q")

search_input_box.send_keys("selenium webdriver")

sleep(2)

print("Clearing search query...")
search_input_box.clear()

sleep(2)

driver.quit()
