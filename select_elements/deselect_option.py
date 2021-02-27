import os
from time import sleep
from selenium.webdriver.support.select import Select
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")

html_page = "file://" + os.getcwd() + "/deselect_option.html"
driver.get(html_page)

select_element = driver.find_element_by_id("langs")

select_object = Select(select_element)

print(f"Multiple selections enabled: {select_object.is_multiple}")

# print all options
print("All options")
for option in select_object.options:
    print(option.text)

sleep(1)

# select three options
select_object.select_by_index(0)
select_object.select_by_value("js")
select_object.select_by_visible_text("Python")

# print all selected options
print("\nSelected options")
for option in select_object.all_selected_options:
    print(option.text)

sleep(1)

# deselect first option
select_object.deselect_by_index(0)

# print all selected options
print("\nSelected options after first deselect")
for option in select_object.all_selected_options:
    print(option.text)

sleep(1)

# deselect all selected options
print("\nDeselect all selected options")
select_object.deselect_all()

print(f"Number of selected options: {len(select_object.all_selected_options)}")

sleep(2)

driver.quit()
