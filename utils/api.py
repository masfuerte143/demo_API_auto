import allure

from utils.http_methods import HttpMethods

base_url = "https://rahulshettyacademy.com"  # Base URL
key = "?key=qaclick123"  # Параметр для всех запросов


class GoogleMapsAPI:
    """Методы для тестирования Google Maps API"""

    @staticmethod
    @allure.step("Создать локацию (Отправить метод POST)")
    def create_new_palace():
        """Метод для создания новой локации"""
        post_resource = "/maps/api/place/add/json"  # ресурс метода пост
        json_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_url = base_url + post_resource + key
        result_post = HttpMethods.post(post_url, json_create_new_place)
        return result_post

    @staticmethod
    @allure.step("Получить данные о локации (Отправить метод GET)")
    def get_new_palace(place_id):
        """Метод для проверки новой локации"""
        get_resource = "/maps/api/place/get/json"  # ресурс метода get
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        result_get = HttpMethods.get(get_url)
        return result_get

    @staticmethod
    @allure.step("Обновить данные о локации (Отправить метод PUT)")
    def update_new_palace(place_id):
        """Метод для изменения новой локации"""
        put_resource = "/maps/api/place/update/json"  # ресурс метода put
        put_url = base_url + put_resource + key
        json_create_new_place = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = HttpMethods.put(put_url, json_create_new_place)
        return result_put

    @staticmethod
    @allure.step("Удалить локацию (Отправить метод DELETE)")
    def delete_new_palace(place_id):
        """Метод для удаления новой локации"""
        del_resource = "/maps/api/place/delete/json"  # ресурс метода delete
        del_url = base_url + del_resource + key
        json_delete_new_place = {
            "place_id": place_id
        }
        result_del = HttpMethods.delete(del_url, json_delete_new_place)
        return result_del
