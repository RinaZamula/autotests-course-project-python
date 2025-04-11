from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://www.youtube.com")

SUBSCRIPTION_BUTTON = (By.XPATH, "//a[@title='Подписки']")
wait.until(EC.element_to_be_clickable(SUBSCRIPTION_BUTTON)).click()

driver.switch_to.new_window("tab")
driver.get("https://habr.com/ru/feed/")

ALL_BUTTON = (By.XPATH, "//a[text()='Все потоки']")
wait.until(EC.element_to_be_clickable(ALL_BUTTON)).click()

driver.switch_to.new_window("window")
driver.get("https://www.youtube.com")

SUBSCRIPTION_BUTTON = (By.XPATH, "//a[@title='Подписки']")
wait.until(EC.element_to_be_clickable(SUBSCRIPTION_BUTTON)).click()