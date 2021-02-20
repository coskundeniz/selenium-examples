from selenium.common.exceptions import ElementNotInteractableException
from webdriver_setup import get_webdriver_for
from time import sleep


driver = get_webdriver_for("firefox")
driver.get("https://www.python.org/")

# create a simple alert with text "Custom Alert"
create_alert = "alert('Custom Alert');"
driver.execute_script(create_alert)

sleep(2)

# switch to alert
alert = driver.switch_to.alert

# try to send keys
try:
    alert.send_keys("Python")
except ElementNotInteractableException as e:
    print(f"Received ElementNotInteractableException with message: {e.args[0]}")

    # close alert and give control to parent
    alert.accept()

    # quit browser
    driver.quit()
