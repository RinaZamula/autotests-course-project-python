import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/select-menu")

DROPDOWN_INPUT_SELECTOR = (By.XPATH, "//input[@id='react-select-3-input']")
DROPDOWN_INPUT_OPTION_SELECTOR = (By.XPATH, "//div[@id='react-select-3-option-0-4']")
DROPDOWN_MULTIPLE_OPTION_SELECTOR = (By.XPATH, "//input[@id='react-select-4-input']")

# Выбор элемента вводом текста в поле
dropdown_field = wait.until(EC.visibility_of_element_located(DROPDOWN_INPUT_SELECTOR))
dropdown_field.send_keys("Dr." + Keys.ENTER)
time.sleep(3)

# Нажатие на элемент в выпадающем списке
dropdown_field.click()
wait.until(EC.visibility_of_element_located(DROPDOWN_INPUT_OPTION_SELECTOR)).click()
time.sleep(3)

# Множественный выбор
dropdown_multiple_option_field = wait.until(EC.visibility_of_element_located(DROPDOWN_MULTIPLE_OPTION_SELECTOR))
dropdown_multiple_option_field.send_keys("Black")
assert dropdown_multiple_option_field.get_attribute("value") == "Black", "Ошибка ввода текста"
dropdown_multiple_option_field.send_keys(Keys.ENTER)
time.sleep(3)

dropdown_multiple_option_field.send_keys("Red")
assert dropdown_multiple_option_field.get_attribute("value") == "Red", "Ошибка ввода текста"
dropdown_multiple_option_field.send_keys(Keys.TAB)
time.sleep(3)