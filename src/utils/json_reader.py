import json
import os


class JsonReader:
    def __init__(self):
        project_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "resources")
        )
        self.json_file_path = os.path.join(project_root, "test_data.json")
        self.data = None

    def _read_json_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
                return json.loads(file_content)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from file {file_path}: {e}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred while reading file {file_path}: {e}")

    def get_data(self):
        if self.data is None:
            self.data = self._read_json_file(self.json_file_path)
        return self.data

    def get_first_name(self):
        data = self.get_data()
        return data.get('first_name', None)

    def get_last_name(self):
        data = self.get_data()
        return data.get('last_name', None)

    def get_email(self):
        data = self.get_data()
        return data.get('email', None)

    def get_current_address(self):
        data = self.get_data()
        return data.get('current_address', None)

    def get_subjects(self):
        data = self.get_data()
        return data.get('subjects', None)

    def get_birth_date(self):
        data = self.get_data()
        birth_date = data.get('birth_date', {})
        return {
            'day': birth_date.get('day', ''),
            'month': birth_date.get('month', ''),
            'year': birth_date.get('year', '')
        }

    def get_image_path(self):
        data = self.get_data()
        return data.get('file_path', None)

    def get_mob_phone(self):
        data = self.get_data()
        return data.get('mobile_phone', None)