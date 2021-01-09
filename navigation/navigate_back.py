from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")

driver.get("https://www.pythondoctor.com/")

# check the url of the page
assert driver.current_url == "https://www.pythondoctor.com/"

# click to second item in the top navigation
driver.find_element_by_css_selector("a.nav-item:nth-child(2)").click()

# check the url of the clicked link
assert driver.current_url == "https://www.pythondoctor.com/bopi/"

# go back to main page
driver.back()

# check if the url of the page changed to main page url
assert driver.current_url == "https://www.pythondoctor.com/"

# quit browser
driver.quit()
