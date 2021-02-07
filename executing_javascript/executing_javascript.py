from selenium.common.exceptions import JavascriptException
from webdriver_setup.get_webdriver import get_webdriver_for
from time import sleep


driver = get_webdriver_for("firefox")
driver.get("https://www.pythondoctor.com/bopi/")

sleep(1)

# remove header from page
remove_header = """
header = document.getElementsByTagName("header")[0];
header.style.display = "none";
"""
driver.execute_script(remove_header)

sleep(1)

# change the color of background
change_background = "document.body.style.background = '#ccc';"
driver.execute_script(change_background)

sleep(1)

# scroll to bottom of the page
scroll_to_bottom = "window.scrollTo(0, document.body.scrollHeight);"
driver.execute_script(scroll_to_bottom)

sleep(3)

# scrollTo was changed as scrollT to get an exception
try:
    scroll_to_bottom = "window.scrollT(0, document.body.scrollHeight);"
    driver.execute_script(scroll_to_bottom)
except JavascriptException as e:
    print(e)
finally:
    driver.quit()
