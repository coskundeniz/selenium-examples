import pickle
from time import sleep
from webdriver_setup import get_webdriver_for


driver = get_webdriver_for("firefox")
driver.get("https://www.google.com")

cookie1 = {"name": "cookie1", "value": "test1", "secure": True}
cookie2 = {"name": "cookie2", "value": "test2", "secure": True}
driver.add_cookie(cookie1)
driver.add_cookie(cookie2)

with open("stored_cookies.pkl", "wb") as cookies:
    pickle.dump(driver.get_cookies(), cookies)

driver.quit()

sleep(3)

driver = get_webdriver_for("firefox")
driver.get("https://www.google.com")

with open("stored_cookies.pkl", "rb") as stored_cookies:
    cookies = pickle.load(stored_cookies)

for cookie in cookies:
    driver.add_cookie(cookie)

for cookie in driver.get_cookies():
    print(f"Name: {cookie['name']}, Value: {cookie['value']}")

sleep(2)

driver.quit()
