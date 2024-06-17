import allure
import pytest

from utils.api import GoogleMapsAPI
from utils.checking import Checking


@allure.parent_suite("Smoke")
class TestBaseGoogleMapsAPI:
    """Тестирование CRUD методов"""

    @pytest.mark.smoke
    @allure.suite("CRUD тесты")
    @allure.title("Новая локация создается")
    def test_creation_new_location(self):
        result_post_method = GoogleMapsAPI.create_new_palace()  # Вызываем метод для создания новой локации в картах
        Checking.check_status_code(result_post_method, 200)  # Проверяем статус код
        Checking.check_json_keys(result_post_method, ['status', 'place_id', 'scope', 'reference',
                                                      'id'])  # Проверяем наличие ключей в json ответа
        Checking.check_json_value(result_post_method, "status", "OK")  # Проверяем значение ключа status

    @pytest.mark.smoke
    @allure.suite("CRUD тесты")
    @allure.title("Данные по созданной локации возвращаются")
    def test_get_created_place(self):
        result_post_method = GoogleMapsAPI.create_new_palace()
        post_json = result_post_method.json()
        place_id = post_json.get("place_id")
        result_get_method = GoogleMapsAPI.get_new_palace(place_id)
        Checking.check_status_code(result_get_method, 200)
        Checking.check_json_keys(result_get_method,
                                 ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                  'language'])
        Checking.check_json_value(result_get_method, "name", "Frontline house")

    @pytest.mark.smoke
    @allure.suite("CRUD тесты")
    @allure.title("Данные по созданной локации обновляются")
    def test_update_created_place(self):
        result_post_method = GoogleMapsAPI.create_new_palace()
        post_json = result_post_method.json()
        place_id = post_json.get("place_id")
        result_put_method = GoogleMapsAPI.update_new_palace(place_id)
        Checking.check_status_code(result_put_method, 200)
        Checking.check_json_keys(result_put_method, ['msg'])
        Checking.check_json_value(result_put_method, "msg", "Address successfully updated")

    @pytest.mark.smoke
    @allure.suite("CRUD тесты")
    @allure.title("Созданная локация удаляется")
    def test_delete_created_place(self):
        result_post_method = GoogleMapsAPI.create_new_palace()
        post_json = result_post_method.json()
        place_id = post_json.get("place_id")
        result_delete_method = GoogleMapsAPI.delete_new_palace(place_id)
        Checking.check_status_code(result_delete_method, 200)
        Checking.check_json_keys(result_delete_method, ['status'])
        Checking.check_json_value(result_delete_method, "status", "OK")
