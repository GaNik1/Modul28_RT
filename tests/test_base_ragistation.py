
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from settings import url_rtk, url_chromedriver
from locators import LOCATOR_NAME, LOCATOR_LAST_NAME, LOCATOR_ID_REGISTRATION
from locators import LOCATOR_ID_PPHONE, LOCATOR_ID_PASSS
from locators import LOCATOR_NAME_SABMIT, LOCATOR_ID_CONF_PASSS


def test_reg_data(name, last_name, phone, passwrd):
    """Регистрируемся"""

    service = Service(url_chromedriver)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url_rtk)
    time.sleep(5)

    driver.find_element(By.ID, LOCATOR_ID_REGISTRATION).click() # Кликаем по регистрации
    time.sleep(3)
    reg_name = driver.find_element(By.NAME, LOCATOR_NAME) # Вводим имя
    reg_name.click()
    time.sleep(1)
    reg_name.send_keys(name)

    reg_last_name = driver.find_element(By.NAME, LOCATOR_LAST_NAME) # Вводим фамилию
    reg_last_name.click()
    time.sleep(1)
    reg_last_name.send_keys(last_name)

    reg_phone = driver.find_element(By.ID, LOCATOR_ID_PPHONE)  # Вводим телефон
    reg_phone.click()
    time.sleep(1)
    reg_phone.send_keys(phone)

    reg_passs = driver.find_element(By.ID, LOCATOR_ID_PASSS)  # Вводим парол
    reg_passs.click()
    time.sleep(2)
    reg_passs.send_keys(passwrd)

    reg_conf_pass = driver.find_element(By.ID, LOCATOR_ID_CONF_PASSS)  # Вводим верификацию пароля
    reg_conf_pass.click()
    time.sleep(3)
    reg_conf_pass.send_keys(passwrd)

    reg_sabmit = driver.find_element(By.NAME, LOCATOR_NAME_SABMIT)  # Вводим верификацию пароля
    reg_sabmit.click()
    time.sleep(3)

    page = driver.page_source
    time.sleep(5)
    driver.close()

    if "Учетные данные" in page:
        # Если страница с данными успешно создана, вернет 1
        exp = 1
        return exp

    elif "Учётная запись уже существует" in page:
        # Если страница с данными уже была создана успешно, вернет 2
        exp = 2
        return exp

    else:
        # Если, при валидном заполнении полней, страница не создается, вернет 0
        exp = 0
        return exp
