from selenium.webdriver.support.events import (AbstractEventListener,
                                               EventFiringWebDriver)
from webdriver_setup import get_webdriver_for
from time import sleep


class CustomEventListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):

        print(f"Before navigating to {url}")
        print(f"Current url before navigating to {url} is '{driver.current_url}'")
        print(f"Page title before navigating to {url} is '{driver.title}'\n")

    def after_navigate_to(self, url, driver):

        print(f"After navigating to {url}")
        print(f"Current url after navigating to {url} is '{driver.current_url}'")
        print(f"Page title after navigating to {url} is '{driver.title}'\n")

    def before_find(self, by, value, driver):

        print(f"Searching for element with '{by}={value}' on {driver.current_url}\n")

    def after_find(self, by, value, driver):

        print(f"Found element with '{by}={value}' on {driver.current_url}\n")

    def before_quit(self, driver):

        print(f"Quitting the browser with url: {driver.current_url}")
        print("Bye ...\n")

    def after_quit(self, driver):

        print("Quit the browser. Have a nice day :)")


driver = get_webdriver_for("firefox")
event_listener = CustomEventListener()

event_firing_driver = EventFiringWebDriver(driver, event_listener)
event_firing_driver.get("https://www.pythondoctor.com/")

mail_input_field = event_firing_driver.find_element_by_id("id_questioner")

sleep(4)

event_firing_driver.quit()
