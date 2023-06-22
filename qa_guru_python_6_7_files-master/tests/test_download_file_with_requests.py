import os.path

import requests
# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь
url = 'https://selenium.dev/images/selenium_logo_square_green.png'

response = requests.get(url)
with open('selenium_logo.png', 'wb') as file:
    file.write(response.content)

size = os.path.getsize('selenium_logo.png')

