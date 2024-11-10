from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.driver_singleton import DriverSingleton


class Wait:
    def __init__(self):
        self._driver = DriverSingleton.get_driver()
        self._wait = WebDriverWait(self._driver, 30)

    def wait_until_element_to_be_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))

    def wait_until_element_to_be_visible(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))
