from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")

driver.get("https://www.pythondoctor.com")

mail_input = driver.find_element_by_id("id_questioner")
print(f"Mail input field placeholder: {mail_input.get_property('placeholder')}")

submit_button = driver.find_element_by_name("submit")
print(f"Submit button text: {submit_button.get_property('value')}")

second_link = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/a[2]")
print(f"Second link text: {second_link.text}")

python_official_link = driver.find_element_by_link_text("Python Official")
print(f"Python Official link text: {python_official_link.text}")

links_container = driver.find_element_by_class_name("list-group")
filtered_links = links_container.find_elements_by_partial_link_text("Python")
for index, link in enumerate(filtered_links, start=1):
    print(f"Link text - {index}: {link.text}")

question_text_area = driver.find_elements_by_tag_name("textarea")[2]
print(f"Question text area placeholder: {question_text_area.get_property('placeholder')}")

nav_items = driver.find_elements(By.CLASS_NAME, "nav-item")
for index, item in enumerate(nav_items, start=1):
    print(f"Navigation item - {index}: {item.text}")

support_button = driver.find_element_by_css_selector("a.btn")
print(f"Support button text: {support_button.text}")

# handle exception
try:
    h1_element = driver.find_element_by_tag_name("h1")
except NoSuchElementException:
    print("There is no h1 tag in the document!")

driver.quit()
