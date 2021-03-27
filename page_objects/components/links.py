
class Links:

    def __init__(self, driver):

        self.driver = driver

    def open_link(self, index):

        link_locator = f"a.list-group-item:nth-child({index})"

        link_at_index = self.driver.find_element_by_css_selector(link_locator)
        link_at_index.click()

    def get_link_count(self):

        return len(self.driver.find_elements_by_class_name("list-group-item"))
