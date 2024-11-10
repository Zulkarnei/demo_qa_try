from selenium import webdriver


class DriverSingleton:
    _drivers = {}


    @classmethod
    def get_driver(cls, browser_name="chrome"):
        if browser_name not in cls._drivers:
            if browser_name == "chrome":
                cls._drivers[browser_name] = webdriver.Chrome()
            elif browser_name == "firefox":
                cls._drivers[browser_name] = webdriver.Firefox()
            elif browser_name == "edge":
                cls._drivers[browser_name] = webdriver.Edge()
            else:
                raise ValueError(f"Browser '{browser_name}' is not supported")

            cls._drivers[browser_name].maximize_window()
        return cls._drivers[browser_name]

    @classmethod
    def quit_driver(cls):
        for driver in cls._drivers.values():
            driver.quit()
        cls._drivers.clear()
