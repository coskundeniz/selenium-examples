import os
from time import sleep
from selenium.webdriver.support.select import Select
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")

html_page = "file://" + os.getcwd() + "/select_option.html"
driver.get(html_page)

select_element = driver.find_element_by_id("langs")

select_object = Select(select_element)

# print all options
for option in select_object.options:
    print(option.text)

sleep(1)

# select option with Python text
select_object.select_by_visible_text("Python")

sleep(2)

# print selected option
print(f"\nSelected option: {select_object.first_selected_option.text}")

driver.quit()
