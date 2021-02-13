from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")
driver.get("https://www.google.com")

cookie_data = {'name': 'customCookie', 'value': 'test', 'secure': True}
driver.add_cookie(cookie_data)

# get the value of newly added cookie
print(f"customCookie value: {driver.get_cookie('customCookie')['value']}")

driver.quit()
