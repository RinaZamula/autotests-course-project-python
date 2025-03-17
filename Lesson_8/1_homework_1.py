# Задание 1:
#
# Заполнить все текстовые поля данными (почистить поля перед заполнением).
# Проверить, что данные действительно введены, используя get_attribute() и assert.
# Страница для выполнения задания: https://demoqa.com/text-box

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/automation-practice-form")

first_name_field = driver.find_element(By.XPATH, "//input[@id='firstName']")
first_name_field.clear()
first_name_field.send_keys("Viktor")
assert first_name_field.get_attribute("value") == "Viktor", "Неверный текст в поле First Name"

last_name_field = driver.find_element(By.XPATH, "//input[@id='lastName']")
last_name_field.clear()
last_name_field.send_keys("Grachev")
assert last_name_field.get_attribute("value") == "Grachev", "Неверный текст в поле Last Name"

email_field = driver.find_element(By.XPATH, "//input[@id='userEmail']")
email_field.clear()
email_field.send_keys("v_grachev1515@yandex.ru")
assert email_field.get_attribute("value") == "v_grachev1515@yandex.ru", "Неверный текст в поле Email"

mobile_field = driver.find_element(By.XPATH, "//input[@id='userNumber']")
mobile_field.clear()
mobile_field.send_keys("+712345678")
assert mobile_field.get_attribute("value") == "+712345678", "Неверный текст в поле Mobile Number"

subject_field = driver.find_element(By.XPATH, "//input[@id='subjectsInput']")
mobile_field.clear()
subject_field.send_keys("math")
assert subject_field.get_attribute("value") == "math", "Неверный текст в поле Subject"

time.sleep(3)

