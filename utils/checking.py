import json


class Checking:
    @staticmethod
    def check_status_code(response, status_code):
        """Проверка статус кода"""
        assert status_code == response.status_code, "Ошибка!"

    @staticmethod
    def check_json_keys(response, expected_value):
        """Метод для проверки обязательных полей"""
        token = json.loads(response.text)
        assert list(token) == expected_value, "Ошибка!"

    @staticmethod
    def check_json_value(response, field_name, expected_value):
        """Метод для проверки значений обязательных полей в ответе запроса"""
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, "Ошибка!"
