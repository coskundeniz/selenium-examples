from time import sleep
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")

driver.get("https://www.pythondoctor.com")

sleep(3)

# set window size as 600x300 px
driver.set_window_size(600, 300)

sleep(2)

# move window to x=0 and y=300 point
driver.set_window_position(0, 300)

sleep(2)

driver.quit()
