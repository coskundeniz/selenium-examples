from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_setup import get_webdriver_for
from time import sleep


driver = get_webdriver_for("firefox")

driver.get("https://www.pythondoctor.com/")

# setup wait for later use
wait = WebDriverWait(driver, 5)

# store the ID of the original window
original_window_handle = driver.current_window_handle

# check only one window is open
assert len(driver.window_handles) == 1

# click to first link in the links section of the page
driver.find_element_by_link_text("Python Official").click()

# wait for the new window or tab
wait.until(EC.number_of_windows_to_be(2))

# Loop through until we find a new window handle and switch to it
for window_handle in driver.window_handles:
    if window_handle != original_window_handle:
        driver.switch_to.window(window_handle)
        break

sleep(3)

# check if the window handle is changed
assert driver.current_window_handle != original_window_handle

driver.quit()
