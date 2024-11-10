import os
import random
import allure

from selenium.webdriver.common.by import By
from src.forms.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class DemoQaPracticeForm(BasePage):
    FIRST_NAME_XPATH = "//input[@id='firstName']"
    LAST_NAME_XPATH = "//input[@id='lastName']"
    MOBILE_NUMBER_XPATH = "//input[@id='userNumber']"
    EMAIL_INPUT_XPATH = "//input[@id='userEmail']"
    ADDRESS_TEXTAREA_XPATH = "//textarea[@id='currentAddress']"
    FILE_INPUT_XPATH = "//input[@id='uploadPicture']"
    SUBMIT_BUTTON_XPATH = "//*[@id='submit']"
    DATE_INPUT_XPATH = "//input[@id='dateOfBirthInput']"
    HOBBIES_CHECKBOXES_XPATHS = {
        "Sports": "//label[@for='hobbies-checkbox-1']",
        "Reading": "//label[@for='hobbies-checkbox-2']",
        "Music": "//label[@for='hobbies-checkbox-3']",
    }
    GENDER_XPATHS = {
        "Male": "//label[@for='gender-radio-1']",
        "Female": "//label[@for='gender-radio-2']",
        "Other": "//label[@for='gender-radio-3']"
    }


    @allure.step("Choose random gender")
    def choose_random_gender(self):
        gender = random.choice(list(self.GENDER_XPATHS.keys()))
        gender_xpath = self.GENDER_XPATHS[gender]
        gender_label = self.driver.find_element(By.XPATH, gender_xpath)
        gender_label.click()
        return gender_label.text

    @allure.step("Open the date picker")
    def open_date_picker(self):
        date_input_element = self.driver.find_element(By.XPATH, self.DATE_INPUT_XPATH)
        self.wait.wait_until_element_to_be_clickable(date_input_element)
        date_input_element.click()
    @allure.step("Set first name")
    def set_first_name(self, first_name):
        first_name_input = self.driver.find_element(By.XPATH, self.FIRST_NAME_XPATH)
        first_name_input.send_keys(first_name)
    @allure.step("Set last name")
    def set_last_name(self, last_name):
        last_name_input = self.driver.find_element(By.XPATH, self.LAST_NAME_XPATH)
        last_name_input.send_keys(last_name)

    @allure.step("Set mobile number")
    def set_mobile_number(self, mobile_number):
        mobile_number_input = self.driver.find_element(By.XPATH, self.MOBILE_NUMBER_XPATH)
        mobile_number_input.send_keys(mobile_number)

    @allure.step("Select random hobby")
    def select_random_hobby(self):
        random_hobby = random.choice(list(self.HOBBIES_CHECKBOXES_XPATHS.values()))

        hobby_label = self.driver.find_element(By.XPATH, random_hobby)
        hobby_label.click()
        return hobby_label.text

    @allure.step("Upload file")
    def upload_file(self, file_path):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
        abs_path = os.path.join(base_dir, file_path)

        if os.path.exists(abs_path):
            file_input = self.driver.find_element(By.XPATH, self.FILE_INPUT_XPATH)
            file_input.send_keys(abs_path)
        else:
            raise FileNotFoundError(f"The file at path {abs_path} does not exist or is not provided.")

    @allure.step("Enter address")
    def enter_address(self, address):
        address_textarea = self.driver.find_element(By.XPATH, self.ADDRESS_TEXTAREA_XPATH)
        self.wait.wait_until_element_to_be_clickable(address_textarea)
        address_textarea.send_keys(address)

    @allure.step("Click submit button")
    def click_submit(self):
        submit_button = self.driver.find_element(By.XPATH, self.SUBMIT_BUTTON_XPATH)
        self.wait.wait_until_element_to_be_clickable(submit_button)
        submit_button.click()

    @allure.step("Set email")
    def set_email(self, first_name):
        first_name_input = self.driver.find_element(By.XPATH, self.EMAIL_INPUT_XPATH)
        first_name_input.send_keys(first_name)
