from utils.http_methods import HttpMethods

base_url = "https://rahulshettyacademy.com"  # Base URL
key = "?key=qaclick123"  # Параметр для всех запросов


class GoogleMapsAPI:
    """Методы для тестирования Google Maps API"""

    @staticmethod
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
        print(post_url)
        result_post = HttpMethods.post(post_url, json_create_new_place)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_new_palace(place_id):
        """Метод для проверки новой локации"""
        get_resource = "/maps/api/place/get/json"  # ресурс метода get
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def update_new_palace(place_id):
        """Метод для изменения новой локации"""
        put_resource = "/maps/api/place/update/json"  # ресурс метода put
        put_url = base_url + put_resource + key
        print(put_url)
        json_create_new_place = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = HttpMethods.put(put_url, json_create_new_place)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_new_palace(place_id):
        """Метод для удаления новой локации"""
        del_resource = "/maps/api/place/delete/json"  # ресурс метода delete
        del_url = base_url + del_resource + key
        print(del_url)
        json_delete_new_place = {
            "place_id": place_id
        }
        result_del = HttpMethods.put(del_url, json_delete_new_place)
        print(result_del.text)
        return result_del
