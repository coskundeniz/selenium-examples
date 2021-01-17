from webdriver_setup import get_webdriver_for
from time import sleep


driver = get_webdriver_for("firefox")

driver.get("https://www.pythondoctor.com")

sleep(5)

mail_input = driver.find_element_by_id("id_questioner")

# send keys to mail input field
mail_input.send_keys("example@somedomain.com")

sleep(2)

driver.quit()
