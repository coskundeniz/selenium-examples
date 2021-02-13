from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")
driver.get("https://www.google.com")

for cookie in driver.get_cookies():
    print(cookie)

print(f"NID cookie value: {driver.get_cookie('NID')['value']}")

driver.quit()
