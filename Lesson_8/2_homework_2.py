# Задание 2:
# Прокликать все ссылки со статус-кодами на странице, используя алгоритм перебора элементов.
# После каждого клика возвращаться на стартовую страницу.
# Страница для выполнения задания: http://the-internet.herokuapp.com/status_codes

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/status_codes")

a_list = driver.find_elements(By.XPATH, "//li/a")

for a in a_list:
    a.click()
    time.sleep(3)
    driver.back()
