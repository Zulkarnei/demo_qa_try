import requests
import allure


class DemoQaApi:
    def authorized(self, base_url, username, password, token=None):
        endpoint = f"{base_url}/Account/v1/Authorized"
        request_body = {
            "userName": username,
            "password": password
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        allure.attach(str(request_body), name="Authorized Request Body", attachment_type=allure.attachment_type.JSON)
        allure.attach(str(headers), name="Authorized Request Headers", attachment_type=allure.attachment_type.JSON)

        response = requests.post(url=endpoint, headers=headers, json=request_body)

        allure.attach(str(response.json()), name="Authorized Response", attachment_type=allure.attachment_type.JSON)

        response.raise_for_status()

        return response.json()

    def generate_token(self, base_url, username, password):
        endpoint = f"{base_url}/Account/v1/GenerateToken"
        request_body = {
            "userName": username,
            "password": password
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        allure.attach(str(request_body), name="Generate Token Request Body", attachment_type=allure.attachment_type.JSON)
        allure.attach(str(headers), name="Generate Token Request Headers", attachment_type=allure.attachment_type.JSON)

        response = requests.post(url=endpoint, headers=headers, json=request_body)

        allure.attach(str(response.json()), name="Generate Token Response", attachment_type=allure.attachment_type.JSON)

        response.raise_for_status()

        return response.json()

    def create_user(self, base_url, username, password):
        endpoint = f"{base_url}/Account/v1/User"
        request_body = {
            "userName": username,
            "password": password
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        allure.attach(str(request_body), name="Create User Request Body", attachment_type=allure.attachment_type.JSON)
        allure.attach(str(headers), name="Create User Request Headers", attachment_type=allure.attachment_type.JSON)

        response = requests.post(url=endpoint, headers=headers, json=request_body)

        allure.attach(str(response.json()), name="Create User Response", attachment_type=allure.attachment_type.JSON)

        response.raise_for_status()

        return response.json()

    def get_user_by_uuid(self, base_url, token, uuid):
        endpoint = f"{base_url}/Account/v1/User/{uuid}"
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }

        allure.attach(str(headers), name="Get User Request Headers", attachment_type=allure.attachment_type.JSON)

        response = requests.get(url=endpoint, headers=headers)

        allure.attach(str(response.json()), name="Get User Response", attachment_type=allure.attachment_type.JSON)

        response.raise_for_status()

        return response.json()

    def delete_user(self, base_url, uuid, token):
        endpoint = f"{base_url}/Account/v1/User/{uuid}"
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }

        allure.attach(str(headers), name="Delete User Request Headers", attachment_type=allure.attachment_type.JSON)

        response = requests.delete(url=endpoint, headers=headers)

        allure.attach(str(response.status_code), name="Delete User Response", attachment_type=allure.attachment_type.TEXT)

        response.raise_for_status()

        return response.status_code
