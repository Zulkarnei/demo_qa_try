import os

import allure
import pytest


@pytest.mark.usefixtures("driver", "setup_ui", "setup_data")
class TestDemoQaPracticeForm:
    @allure.story("Fill and Submit the Practice Form")
    @allure.step("Fill out and submit the form")
    def test_fill_and_submit_form(self, driver, setup_ui, setup_data):
        driver_utils, practice_form, calendar_form, thx_form = setup_ui
        data = setup_data

        practice_form.set_first_name(data["first_name"])
        practice_form.set_last_name(data["last_name"])
        practice_form.set_email(data["email"])
        practice_form.set_mobile_number(data["mobile_phone"])

        practice_form.open_date_picker()
        calendar_form.select_year(data["birth_date"]["year"])
        calendar_form.select_month(data["birth_date"]["month"])
        calendar_form.select_day(data["birth_date"]["day"])

        driver_utils.scroll_to_middle()

        selected_gender = practice_form.choose_random_gender()
        selected_hobby = practice_form.select_random_hobby()
        practice_form.upload_file(data["image_path"])
        practice_form.enter_address(data["current_address"])

        driver_utils.scroll_to_middle()

        practice_form.click_submit()

        success_message = thx_form.get_thanks_text()
        assert "Thanks for submitting the form" in success_message

        with allure.step("Verify success message is displayed"):
            success_message = thx_form.get_thanks_text()
            assert "Thanks for submitting the form" in success_message

        with allure.step("Verify student name"):
            student_name = thx_form.get_student_name()
            assert student_name == data["first_name"] + " " + data[
                "last_name"], f"Expected {data['first_name']} {data['last_name']}, but got {student_name}"

        with allure.step("Verify student email"):
            student_email = thx_form.get_student_email()
            assert student_email == data["email"], f"Expected {data['email']}, but got {student_email}"

        with allure.step("Verify gender"):
            gender = thx_form.get_gender()
            assert gender == selected_gender, f"Expected {selected_gender}, but got {gender}"

        with allure.step("Verify hobby"):
            hobby = thx_form.get_hobby()
            assert hobby == selected_hobby, f"Expected {selected_hobby}, but got {hobby}"

        with allure.step("Verify mobile number"):
            phone_number = thx_form.get_phone_number()
            assert phone_number == data["mobile_phone"], f"Expected {data['mobile_phone']}, but got {phone_number}"

        with allure.step("Verify picture name"):
            picture = thx_form.get_picture()
            expected_picture_name = os.path.basename(data["image_path"])
            assert picture == expected_picture_name, f"Expected {data['image_path'].split('\\')[-1]}, but got {picture}"

        with allure.step("Verify date of birth"):
            birth_date = thx_form.get_birth_date()
            expected_birth_date = f"{data['birth_date']['day']} {data['birth_date']['month']},{data['birth_date']['year']}"

            assert birth_date == expected_birth_date, f"Expected {expected_birth_date}, but got {birth_date}"

        with allure.step("Verify address"):
            address = thx_form.get_address()
            assert address == data["current_address"], f"Expected {data['current_address']}, but got {address}"

