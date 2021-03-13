from webdriver_setup import get_webdriver_for
from time import sleep


driver = get_webdriver_for("firefox")

driver.get("https://www.pythondoctor.com")

sleep(4)

# returns base64 encoded string into image
driver.save_screenshot("./home_page.png")

driver.quit()
