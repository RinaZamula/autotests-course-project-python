from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")

BUTTON_ENABLED = (By.XPATH, "//button[@id='enableAfter']")

wait.until(EC.element_to_be_clickable(BUTTON_ENABLED))
driver.find_element(*BUTTON_ENABLED).click()
