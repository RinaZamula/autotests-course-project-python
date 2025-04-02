import os
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/en/us/login")

LOGIN_FIELD = (By.XPATH, "//input[@id='login_email']")
PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
SUBMIT_BUTTON = (By.XPATH, "//button[@id='loginformsubmit']")

# Логинимся в аккаунт
wait.until(EC.visibility_of_element_located(LOGIN_FIELD)).send_keys("autocheck@ya.ru")
wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys("123")
wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON)).click()

# Сохраняем куки в файл
with open(os.getcwd() + "\\cookies\\cookies.pkl", "wb") as write_file:
    pickle.dump(driver.get_cookies(), write_file)

# Очищаем куки и переходим на страницу логина
driver.delete_all_cookies()
driver.get("https://www.freeconferencecall.com/en/us/login")

# Еще раз чистим куки
driver.delete_all_cookies()

cookies = []

# Открываем файл с куками и считываем их в список
with open(os.getcwd() + "\\cookies\\cookies.pkl", "rb") as read_file:
    cookies = pickle.load(read_file)

# В цикле добавляем новые куки по одной
for cookie in cookies:
    driver.add_cookie(cookie)

# Для проверки переходим на страницу, которая доступна только авторизованному пользователю
driver.get("https://www.freeconferencecall.com/profile/settings")
