from time import sleep
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")
driver.get("https://www.python.org/")

# create a simple alert with text "Custom Alert"
create_alert = "alert('Custom Alert');"
driver.execute_script(create_alert)

sleep(1)

# switch to the alert
alert = driver.switch_to.alert

# get the text of the alert
print(f"Alert text: {alert.text}")

# accept the alert
alert.accept()

sleep(2)

driver.quit()
