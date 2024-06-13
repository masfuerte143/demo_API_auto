import json


class Checking:
    @staticmethod
    def check_status_code(response, status_code):
        """Проверка статус кода"""
        assert status_code == response.status_code, "Ошибка!"

    @staticmethod
    def check_json_token(response, expected_value):
        """Метод для проверки обязательных полей"""
        token = json.loads(response.text)
        assert list(token) == expected_value, "Ошибка!"

