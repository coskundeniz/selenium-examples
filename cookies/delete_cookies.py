from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")
driver.get("https://www.google.com")

print(f"Number of cookies before adding cookies: {len(driver.get_cookies())}")

cookie1 = {"name": "cookie1", "value": "test1", "secure": True}
cookie2 = {"name": "cookie2", "value": "test2", "secure": True}
cookie3 = {"name": "cookie3", "value": "test3", "secure": True}
driver.add_cookie(cookie1)
driver.add_cookie(cookie2)
driver.add_cookie(cookie3)

print(f"Number of cookies after adding cookies: {len(driver.get_cookies())}")

driver.delete_cookie("cookie1")

print(f"Number of cookies after deleting a cookie: {len(driver.get_cookies())}")

driver.delete_all_cookies()

print(f"Number of cookies after deleting all cookies: {len(driver.get_cookies())}")

driver.quit()
