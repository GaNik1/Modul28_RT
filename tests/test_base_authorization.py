
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from settings import url_rtk, url_chromedriver
from locators import LOCATOR_ID_USER_NAME, LOCATOR_ID_USER_PASSWORD, LOCATOR_ID_ACCEPT


def test_auth_paswrd(passwrd, auth_number, locator):
    """Удостоверимся что можно зайти с комбинациями логина и пароля"""

    service = Service(url_chromedriver)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url_rtk)
    time.sleep(5)

    driver.find_element(By.ID, locator).click() # Кликаем по закладке
    elem_auth = driver.find_element(By.ID, LOCATOR_ID_USER_NAME) # Присваиваем переменной elem_auth лицевой счет
    elem_auth.click() # Кликаем по лицевому счету
    elem_auth.send_keys(auth_number) # Ввели номер счета
    elem_pass = driver.find_element(By.ID, LOCATOR_ID_USER_PASSWORD) # Присваиваем переменной elem_pass password
    elem_pass.click() # Кликаем по паролю
    elem_pass.send_keys(passwrd) # Ввели пароль
    time.sleep(1)
    driver.find_element(By.ID, LOCATOR_ID_ACCEPT).click() # Жмем принять
    time.sleep(1)
    page = driver.page_source
    time.sleep(3)
    driver.close()

    if "Учетные данные" in page:
        # Если зашел вернет 1
        return 1

    else:
        # Если не зашел вернет 0
        return 0


