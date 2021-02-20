from time import sleep
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")
driver.get("https://www.python.org/")

# create a prompt alert
create_prompt_alert = "prompt('What is your favourite programming language?');"
driver.execute_script(create_prompt_alert)

# switch to alert
alert = driver.switch_to.alert

sleep(1)

# fill the text input field
alert.send_keys("Python")

sleep(2)

alert.accept()

driver.quit()
