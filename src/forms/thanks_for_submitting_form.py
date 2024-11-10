import allure
from selenium.webdriver.common.by import By
from src.forms.pages.base_page import BasePage


class ThanksForSubmittingForm(BasePage):
    SUCCESS_MESSAGE_XPATH = "//div[contains(@class, 'modal-content')]//div[contains(@class, 'modal-header')]"
    STUDENT_NAME_XPATH = "//tr[td[contains(normalize-space(text()), 'Student') and contains(normalize-space(text()), 'Name')]]//following-sibling::td"
    STUDENT_MAIL_XPATH = "//tr[td[contains(normalize-space(text()), 'Student') and contains(normalize-space(text()), 'Email')]]//following-sibling::td"
    GENDER_XPATH = "//tr[td[contains(normalize-space(text()), 'Gender')]]//following-sibling::td"
    MOBILE_XPATH = "//tr[td[contains(normalize-space(text()), 'Mobile')]]//following-sibling::td"
    PICTURE_XPATH = "//tr[td[contains(normalize-space(text()), 'Picture')]]//following-sibling::td"
    ADDRESS_XPATH = "//tr[td[contains(normalize-space(text()), 'Address')]]//following-sibling::td"
    HOBBIES_XPATH = "//tr[td[contains(normalize-space(text()), 'Hobbies')]]//following-sibling::td"
    BIRTH_DATE_XPATH = "//tr[td[contains(normalize-space(text()), 'Date') and contains(normalize-space(text()), 'of') and contains(normalize-space(text()), 'Birth')]]//following-sibling::td"

    @allure.step("Get success message text")
    def get_thanks_text(self):
        success_message = self.driver.find_element(By.XPATH, self.SUCCESS_MESSAGE_XPATH).text
        return success_message

    @allure.step("Get student name")
    def get_student_name(self):
        value_element = self.driver.find_element(By.XPATH, self.STUDENT_NAME_XPATH)
        value_text = value_element.text
        return value_text

    @allure.step("Get student email")
    def get_student_email(self):
        value_element = self.driver.find_element(By.XPATH, self.STUDENT_MAIL_XPATH)
        value_text = value_element.text
        return value_text

    @allure.step("Get student gender")
    def get_gender(self):
        value_element = self.driver.find_element(By.XPATH, self.GENDER_XPATH)
        value_text = value_element.text
        return value_text

    @allure.step("Get student mobile phone number")
    def get_phone_number(self):
        value_element = self.driver.find_element(By.XPATH, self.MOBILE_XPATH)
        value_text = value_element.text
        return value_text

    @allure.step("Get uploaded picture name")
    def get_picture(self):
        value_element = self.driver.find_element(By.XPATH, self.PICTURE_XPATH)
        value_text = value_element.text
        return value_text

    @allure.step("Get student address")
    def get_address(self):
        value_element = self.driver.find_element(By.XPATH, self.ADDRESS_XPATH)
        value_text = value_element.text
        return value_text

    @allure.step("Get student hobbies")
    def get_hobby(self):
        value_element = self.driver.find_element(By.XPATH, self.HOBBIES_XPATH)
        value_text = value_element.text
        return value_text

    @allure.step("Get student birth date")
    def get_birth_date(self):
        value_element = self.driver.find_element(By.XPATH, self.BIRTH_DATE_XPATH)
        value_text = value_element.text
        return value_text
