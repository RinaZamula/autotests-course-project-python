from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(10)

driver.get("https://demoqa.com/dynamic-properties")

BUTTON_ENABLED = (By.XPATH, "//button[@id='enableAfter']")

driver.find_element(*BUTTON_ENABLED).click()