import os.path
import requests


def test_file_requests():
    # TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'
    response = requests.get(url)
    downloaded_file_full_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tmp', 'selenium_logo.png')
    with open(downloaded_file_full_path, 'wb') as file:
        file.write(response.content)

    assert os.path.getsize(downloaded_file_full_path) == 30803
    os.remove(downloaded_file_full_path)