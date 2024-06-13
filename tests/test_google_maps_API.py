from requests import Response

from utils.api import GoogleMapsAPI


class TestCreatePlace:
    """Создание изменение и удаление новой локации"""
    def test_create_new_place(self):
        print("Метод POST")
        result_post = GoogleMapsAPI.create_new_palace()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        print("Метод GET POST")
        result_get = GoogleMapsAPI.get_new_palace(place_id)
        print("Метод PUT")
        result_put = GoogleMapsAPI.update_new_palace(place_id)
        print("Метод GET PUT")
        result_get = GoogleMapsAPI.get_new_palace(place_id)
        print("Метод DELETE")
        result_del = GoogleMapsAPI.delete_new_palace(place_id)
        print("Метод GET DELETE")
        result_get = GoogleMapsAPI.get_new_palace(place_id)

