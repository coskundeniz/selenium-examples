from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")

driver.get("https://www.pythondoctor.com")

links_section = driver.find_element_by_class_name("list-group")

# returns base64 encoded string into image
links_section.screenshot("./links.png")

driver.quit()
