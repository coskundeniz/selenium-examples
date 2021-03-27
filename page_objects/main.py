from webdriver_setup import get_webdriver_for

from tests.test_home import TestHomePage
from tests.test_bopi import TestBOPIPage


if __name__ == "__main__":

    try:
        driver = get_webdriver_for("firefox")

        home_page_test = TestHomePage(driver)

        home_page_test.test_submit_question()
        home_page_test.test_navigate_to_bopi_page()
        home_page_test.test_navigate_to_about()
        home_page_test.test_navigate_to_feedback()

        bopi_page_test = TestBOPIPage(driver)

        bopi_page_test.test_best_practices_filter()
        bopi_page_test.test_navigate_to_homepage()

        home_page_test.test_open_link(1)

        from time import sleep
        sleep(2)

    except Exception as exp:
        print(exp)
    finally:
        driver.quit()
