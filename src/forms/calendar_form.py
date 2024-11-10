import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from src.forms.pages.base_page import BasePage


class CalendarForm(BasePage):
    MONTH_XPATH = "//select[contains(@class, 'react-datepicker__month-select')]"
    YEAR_XPATH = "//select[contains(@class, 'react-datepicker__year-select')]"
    DAY_XPATH_TEMPLATE = ("//div[contains(@class, 'react-datepicker__day--0{day:02d}') and not(contains(@class, "
                          "'react-datepicker__day--outside-month'))]")

    @allure.step("Select month: {month}")
    def select_month(self, month):
        month_select = Select(self.driver.find_element(By.XPATH, self.MONTH_XPATH))
        month_select.select_by_visible_text(month)

    @allure.step("Select year: {year}")
    def select_year(self, year):
        year_select = Select(self.driver.find_element(By.XPATH, self.YEAR_XPATH))
        year_select.select_by_visible_text(year)

    @allure.step("Select day: {day}")
    def select_day(self, day):
        day_xpath = self.DAY_XPATH_TEMPLATE.format(day=int(day))
        day_element = self.driver.find_element(By.XPATH, day_xpath)
        day_element.click()

