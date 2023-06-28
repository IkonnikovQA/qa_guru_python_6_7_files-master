import time
import os.path

from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp

def clear_directory(path):
    files_list = os.listdir(path)
    for file in files_list:
        os.remove(f'{path}{file}')


def test_file_browser():
    download_dir_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tmp/')
    clear_directory(download_dir_name)
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir_name,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver_options = options
    browser.config.driver = driver
    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(10)
    downloads_content = os.listdir(download_dir_name)
    assert len(downloads_content) == 1
    assert downloads_content[0] == 'pytest-main.zip'
    clear_directory(download_dir_name)