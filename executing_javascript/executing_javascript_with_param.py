from webdriver_setup import get_webdriver_for
from time import sleep

driver = get_webdriver_for("firefox")
driver.get("https://www.pythondoctor.com/")

mail_input = driver.find_element_by_id("id_questioner")

change_input_field_value = "arguments[0].value = 'codenineeight@gmail.com';"

driver.execute_script(change_input_field_value, mail_input)

sleep(5)

driver.quit()
