from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 30, poll_frequency=1)

driver.get("https://omayo.blogspot.com")

# Дождаться появления текста через 10 секунд
TEXT_APPEARS_IN_10_SEC = (By.XPATH, "//div[@id='delayedText']")
wait.until(EC.visibility_of_element_located(TEXT_APPEARS_IN_10_SEC))

# Дождаться исчезновения текста через 25 секунд
TEXT_DISAPPEARS_IN_25_SEC = (By.XPATH, "//div[@id='deletesuccess']")
wait.until(EC.invisibility_of_element_located(TEXT_DISAPPEARS_IN_25_SEC))

# Дождаться состояния enabled для кнопки
BUTTON_DELAYED_ENABLE = (By.XPATH, "//input[@id='timerButton']")
wait.until(EC.element_to_be_clickable(BUTTON_DELAYED_ENABLE))

# Нажать на одну кнопку, чтобы состояние другой стало disabled и проверить это
BUTTON_TRY_IT = (By.XPATH, "//button[text()='Try it']")
BUTTON_DISABLED_AFTER_CLICK = (By.XPATH, "//button[@id='myBtn']")
wait.until(EC.visibility_of_element_located(BUTTON_TRY_IT)).click()
wait.until(EC.element_attribute_to_include(BUTTON_DISABLED_AFTER_CLICK, "disabled"))
