from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()

driver = webdriver.Remote(
    # change ip with your remote machine's address
    command_executor="http://192.168.1.39:4444",
    desired_capabilities=capabilities
)

driver.get("https://www.google.com")

search_input_box = driver.find_element(By.NAME, "q")

search_input_box.send_keys("selenium webdriver" + Keys.ENTER)

sleep(3)

driver.quit()
