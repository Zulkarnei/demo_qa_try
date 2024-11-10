class DriverUtils:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_middle(self):
        total_height = self.driver.execute_script("return document.body.scrollHeight;")
        self.driver.execute_script(f"window.scrollTo(0, {total_height / 2});")
