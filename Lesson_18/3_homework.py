from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.page_load_strategy = "eager"

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

#Открываем три вкладки и открываем в них три разных сайта
driver.get("https://www.youtube.com")

driver.switch_to.new_window("tab")
driver.get("https://habr.com/ru/feed/")

driver.switch_to.new_window("tab")
driver.get("https://ru.pinterest.com")

#Получаем список дескрипторов всех вкладок
tabs_descriptors = driver.window_handles

#Переходим на каждую вкладку и выводим в терминал ее название
driver.switch_to.window(tabs_descriptors[0])
print(f"Первая вкладка: {driver.title}")

driver.switch_to.window(tabs_descriptors[1])
print(f"Вторая вкладка: {driver.title}")

driver.switch_to.window(tabs_descriptors[2])
print(f"Третья вкладка вкладка: {driver.title}")

#Кликаем на один элемент на каждой странице
driver.switch_to.window(tabs_descriptors[0])
SUBSCRIPTION_BUTTON = (By.XPATH, "//a[@title='Подписки']")
wait.until(EC.visibility_of_element_located(SUBSCRIPTION_BUTTON)).click()

driver.switch_to.window(tabs_descriptors[1])
ALL_BUTTON = (By.XPATH, "//a[text()='Все потоки']")
wait.until(EC.visibility_of_element_located(ALL_BUTTON)).click()

driver.switch_to.window(tabs_descriptors[2])
DESCRIPTION_BUTTON = (By.XPATH, "//a[text()='Описание']")
wait.until(EC.visibility_of_element_located(DESCRIPTION_BUTTON)).click()