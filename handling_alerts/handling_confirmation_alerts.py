from time import sleep
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")
driver.get("https://www.python.org/")

# create a confirmation alert
create_confirmation_alert = "confirm('Confirmation Alert Box');"
driver.execute_script(create_confirmation_alert)

sleep(2)

# switch to alert
alert = driver.switch_to.alert

# dismiss/cancel the alert
alert.dismiss()

sleep(2)

driver.quit()
