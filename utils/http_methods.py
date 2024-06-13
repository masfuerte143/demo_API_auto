import requests


class HttpMethods:
    """Список HTTР методов"""
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod  # статичный метод, для вызова где угодно
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod  # статичный метод, для вызова где угодно
    def post(url, body):
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod  # статичный метод, для вызова где угодно
    def put(url, body):
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod  # статичный метод, для вызова где угодно
    def delete(url, body):
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result
