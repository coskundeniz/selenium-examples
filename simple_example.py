from time import sleep
from webdriver_setup import get_webdriver_for


# create driver instance
driver = get_webdriver_for("firefox")

# start the browser with the given url
driver.get("https://www.pythondoctor.com/")

# print the title of the website
print(f"Title: {driver.title}")

# sleep 5 seconds
sleep(5)

# quit browser
driver.quit()
