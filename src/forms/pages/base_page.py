from abc import ABC
from src.waitings.conditional_waits import Wait


class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver
        self.wait = Wait()
