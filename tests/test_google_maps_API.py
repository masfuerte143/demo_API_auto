from requests import Response

from utils.api import GoogleMapsAPI


class TestCreatePlace:
    """Создание изменение и удаление новой локации"""
    def test_create_new_place(self):
        print("Метод ПОСТ")
        result_post = GoogleMapsAPI.create_new_palace()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        print("Метод GET")
        result_get: Response = GoogleMapsAPI.get_new_palace(place_id)

