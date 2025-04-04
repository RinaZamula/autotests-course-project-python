from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/checkbox")

CHECKBOX = (By.XPATH, "//input[@id='tree-node-home']")
SPAN_FOR_CHECKBOX_CLICK = (By.XPATH, "//span[@class='rct-checkbox']")

wait.until(EC.visibility_of_element_located(SPAN_FOR_CHECKBOX_CLICK)).click()
assert driver.find_element(*CHECKBOX).is_selected(), "Чек-бокс еще не нажат"
