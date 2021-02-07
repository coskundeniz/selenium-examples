from webdriver_setup.get_webdriver import get_webdriver_for

driver = get_webdriver_for("firefox")

async_js_code = """
var callback = arguments[arguments.length - 1];

window.setTimeout(function() {
    callback("callback invoked!");
}, 3000);
"""

ret_val = driver.execute_async_script(async_js_code)
print(f"ret_val: {ret_val}")

driver.quit()
