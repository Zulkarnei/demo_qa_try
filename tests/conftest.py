import pytest
import allure
from src.forms.thanks_for_submitting_form import ThanksForSubmittingForm
from src.forms.calendar_form import CalendarForm
from src.forms.pages.demoqa_practice_form_page import DemoQaPracticeForm
from src.utils.driver_singleton import DriverSingleton
from src.api.demoqa_api import DemoQaApi
from src.utils.driver_utils import DriverUtils
from src.utils.json_reader import JsonReader
from src.utils.utils import UserUtils


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="Browser to run tests on: chrome, firefox, or edge"
    )


@pytest.fixture(scope="class")
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = DriverSingleton.get_driver(browser_name)
    yield driver
    DriverSingleton.quit_driver()


@pytest.fixture(scope="class")
@allure.step("Loading setup data from JSON file")
def setup_data():
    json_reader = JsonReader()
    first_name = json_reader.get_first_name()
    last_name = json_reader.get_last_name()
    email = json_reader.get_email()
    current_address = json_reader.get_current_address()
    subjects = json_reader.get_subjects()
    birth_date = json_reader.get_birth_date()
    image_path = json_reader.get_image_path()
    mobile_phone = json_reader.get_mob_phone()

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "current_address": current_address,
        "subjects": subjects,
        "birth_date": birth_date,
        "image_path": image_path,
        "mobile_phone": mobile_phone
    }


@pytest.fixture(scope="class")
@allure.step("Setting up UI components")
def setup_ui(driver, url):
    driver.get(url + "/automation-practice-form")
    driver_utils = DriverUtils(driver)
    practice_form = DemoQaPracticeForm(driver)
    calendar_form = CalendarForm(driver)
    thx_form = ThanksForSubmittingForm(driver)
    return driver_utils, practice_form, calendar_form, thx_form


@pytest.fixture(scope="class")
def url(request):
    return "https://demoqa.com"


@pytest.fixture(scope="class")
@allure.step("Instantiating API client")
def api():
    return DemoQaApi()


@pytest.fixture(scope="function")
@allure.step("Generating random username and password for API user")
def api_user():
    return {
        "username": UserUtils.generate_random_username(),
        "password": "TestUser@1234"
    }
