from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/browser-windows")

#Получаем дескриптор текущей вкладки
current_tab_descriptor = driver.current_window_handle

#Нажимаем на кнопку, которая открывает новую вкладку
TAB_BUTTON = (By.XPATH, "//button[@id='tabButton']")
wait.until(EC.visibility_of_element_located(TAB_BUTTON)).click()

#Получаем дескрипторы всех открытых окон и вкладок, переключаемся на новую вкладку и проверяем это
all_descriptors = driver.window_handles
driver.switch_to.window(all_descriptors[1])
assert current_tab_descriptor != driver.current_window_handle, "Переключения на новую вкладку не произошло"

#Получаем текст с открытой вкладки, чтобы проверить, действительно ли мы на нее переключились
H1_NEW_TAB = (By.XPATH, "//h1")
text = wait.until(EC.visibility_of_element_located(H1_NEW_TAB)).text
assert text in "This is a sample page", "Текст отличается"
