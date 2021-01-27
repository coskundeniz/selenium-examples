from selenium.webdriver import FirefoxOptions
from webdriver_setup import get_webdriver_for

firefox_options = FirefoxOptions()
firefox_options.add_argument("--headless")

driver = get_webdriver_for("firefox", options=firefox_options)
assert driver.capabilities["moz:headless"] == True

driver.get("https://www.pythondoctor.com/")
print(f"Title: {driver.title}")

driver.quit()
