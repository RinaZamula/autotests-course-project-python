from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/selectable")

# Находим вкладку и нажимаем на нее
TAB_GRID = (By.XPATH, "//a[@id='demo-tab-grid']")
wait.until(EC.visibility_of_element_located(TAB_GRID)).click()

# Находим кнопку 5 и нажимаем на нее
OPTION_FIVE = (By.XPATH, "//li[text()='Five']")
option_five = wait.until(EC.visibility_of_element_located(OPTION_FIVE))
option_five.click()

# Проверяем, нажата ли кнопка 5
assert "active" in option_five.get_attribute("class"), "Элемент не нажат"

# Находим кнопку 8 и нажимаем на нее
OPTION_EIGHT = (By.XPATH, "//li[text()='Eight']")
option_eight = wait.until(EC.visibility_of_element_located(OPTION_EIGHT))
option_eight.click()

#Проверяем, нажата ли кнопка 8
assert "active" in option_eight.get_attribute("class"), "Элемент не нажат"

# Снова нажимаем на кнопки 5 и 8, чтобы снять выделение
option_five.click()
option_eight.click()

# Проверяем, снято ли выделение
assert "active" not in option_five.get_attribute("class"), "Элемент нажат"
assert "active" not in option_eight.get_attribute("class"), "Элемент нажат"
