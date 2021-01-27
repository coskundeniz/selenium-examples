from selenium.webdriver import (FirefoxProfile,
                                FirefoxOptions,
                                DesiredCapabilities)
from webdriver_setup import get_webdriver_for
from time import sleep

firefox_options = FirefoxOptions()
firefox_options.log.level = "trace"

capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities['acceptInsecureCerts'] = True
capabilities['loggingPrefs'] = {'browser': 'trace'}

profile = FirefoxProfile()
profile.set_preference("dom.ipc.processCount", 8)
profile.set_preference("browser.startup.page", 1)
profile.set_preference("browser.startup.homepage",
                       "https://www.google.com/")

driver = get_webdriver_for("firefox",
                           capabilities=capabilities,
                           firefox_profile=profile,
                           options=firefox_options)

sleep(3)

driver.quit()
