from webdriver_setup.get_webdriver import get_webdriver_for
from time import sleep

driver = get_webdriver_for("firefox")
driver.get("https://www.pythondoctor.com/")

js_code = "return document.getElementById('id_questioner').placeholder;"
mail_input_placeholder = driver.execute_script(js_code)
print(f"Placeholder: {mail_input_placeholder}")

sleep(4)

driver.quit()
