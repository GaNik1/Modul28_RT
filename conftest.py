import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from settings import url_rtk, url_chromedriver


@pytest.fixture(autouse=True)
def browser():
    service = Service(url_chromedriver)
    driver = webdriver.Chrome(service=service)

    # Переходим на страницу авторизации
    driver.get(url_rtk)

    # Максимизируем окно браузера
    driver.maximize_window()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()