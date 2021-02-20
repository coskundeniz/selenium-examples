from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from webdriver_setup import get_webdriver_for
from time import sleep


driver = get_webdriver_for("firefox")
driver.get("https://www.python.org/")

# create a simple alert with text "Custom Alert" after 3 seconds
create_alert_with_timeout = """
setTimeout(function(){
    alert('Custom Alert');
}, 3000);
"""
driver.execute_script(create_alert_with_timeout)

# switch to alert
try:
    alert = driver.switch_to.alert
except NoAlertPresentException:
    print("Received NoAlertPresentException")

# second switch attempt with explicit wait
try:
    print("Switching to alert with explicit wait")
    wait = WebDriverWait(driver, timeout=5)
    wait.until(EC.alert_is_present(), "Timed out waiting for alert!")

    alert = driver.switch_to.alert
    sleep(2)
    alert.accept()
    print("Closed alert dialog")

except TimeoutException:
    print("Timed out waiting for alert!")
finally:
    driver.quit()
