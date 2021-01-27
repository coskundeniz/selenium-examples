from selenium.webdriver import ChromeOptions, DesiredCapabilities
from webdriver_setup import get_webdriver_for
from time import sleep

chrome_options = ChromeOptions()
chrome_options.add_argument("start-maximized")

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptInsecureCerts'] = True

driver = get_webdriver_for("chrome", desired_capabilities=capabilities, options=chrome_options)

driver.get("https://www.google.com/")

sleep(2)

driver.quit()
