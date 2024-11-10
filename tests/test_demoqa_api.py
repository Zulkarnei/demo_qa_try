import allure
import pytest


@allure.feature("Account API")
@pytest.mark.usefixtures("api", "url", "api_user")
class TestDemoQaApi:
    @allure.story("Create User")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user(self, api, url, api_user):
        create_response = api.create_user(url, api_user["username"], api_user["password"])
        assert create_response["username"] == api_user["username"]
        assert "userID" in create_response

    @allure.story("Non Authorized User")
    @allure.severity(allure.severity_level.NORMAL)
    def test_non_authorized_user(self, api, url, api_user):
        api.create_user(url, api_user["username"], api_user["password"])
        auth_response = api.authorized(url, api_user["username"], api_user["password"])
        assert auth_response is False

    @allure.story("Authorized User")
    @allure.severity(allure.severity_level.NORMAL)
    def test_authorized_user(self, api, url, api_user):
        api.create_user(url, api_user["username"], api_user["password"])
        token = api.generate_token(url, api_user["username"], api_user["password"])["token"]
        auth_response = api.authorized(url, api_user["username"], api_user["password"], token=token)
        assert auth_response is True

    @allure.story("Generate Token")
    @allure.severity(allure.severity_level.NORMAL)
    def test_generate_token(self, api, url, api_user):
        token_response = api.generate_token(url, api_user["username"], api_user["password"])
        assert "token" in token_response

    @allure.story("Get User by UUID")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_user(self, api, url, api_user):
        create_response = api.create_user(url, api_user["username"], api_user["password"])
        uuid = create_response["userID"]
        token_response = api.generate_token(url, api_user["username"], api_user["password"])
        token = token_response["token"]

        user_data = api.get_user_by_uuid(url, token, uuid)
        assert user_data["username"] == api_user["username"]

    @allure.story("Delete User")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_user(self, api, url, api_user):
        create_response = api.create_user(url, api_user["username"], api_user["password"])
        uuid = create_response["userID"]
        token_response = api.generate_token(url, api_user["username"], api_user["password"])
        token = token_response["token"]

        delete_response = api.delete_user(url, uuid, token)
        assert delete_response == 204
