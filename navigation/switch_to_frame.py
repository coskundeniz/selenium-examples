import os
from time import sleep
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")

html_page = "file://" + os.getcwd() + "/iframe_example.html"
driver.get(html_page)

# locate iframe
iframe = driver.find_element_by_css_selector("#iframe_container > iframe")

# switch to iframe
driver.switch_to.frame(iframe)

sleep(3)

# click on the button
driver.find_element_by_tag_name("button").click()

sleep(3)

driver.quit()
