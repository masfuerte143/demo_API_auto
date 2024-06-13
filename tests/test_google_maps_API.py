import json

from utils.api import GoogleMapsAPI
from utils.checking import Checking


class TestCreatePlace:
    """Создание изменение и удаление новой локации"""

    def test_create_new_place(self):
        print("Метод POST")
        result_post = GoogleMapsAPI.create_new_palace()
        check_post = result_post.json()
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        place_id = check_post.get("place_id")
        # token = json.loads(result_post.text)
        # print(list(token))
        print("Метод GET POST")
        result_get = GoogleMapsAPI.get_new_palace(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        # token = json.loads(result_get.text)
        # print(list(token))
        print("Метод PUT")
        result_put = GoogleMapsAPI.update_new_palace(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        print("Метод GET PUT")
        result_get = GoogleMapsAPI.get_new_palace(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        print("Метод DELETE")
        result_del = GoogleMapsAPI.delete_new_palace(place_id)
        Checking.check_status_code(result_del, 200)
        Checking.check_json_token(result_del, ['status'])
        # token = json.loads(result_del.text)
        # print(list(token))
        print("Метод GET DELETE")
        result_get = GoogleMapsAPI.get_new_palace(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])

