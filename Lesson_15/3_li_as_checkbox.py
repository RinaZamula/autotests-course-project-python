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

TAB_GRID = (By.XPATH, "//a[@id='demo-tab-grid']")
wait.until(EC.visibility_of_element_located(TAB_GRID)).click()

OPTION_EIGHT = (By.XPATH, "//li[text()='Eight']")
option_eight = wait.until(EC.visibility_of_element_located(OPTION_EIGHT))
option_eight.click()

assert "active" in option_eight.get_attribute("class"), "Элемент не нажат"
