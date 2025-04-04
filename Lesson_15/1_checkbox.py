from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://the-internet.herokuapp.com/checkboxes")

CHECKBOX_1 = (By.XPATH, "//input[@type='checkbox'][1]")
CHECKBOX_2 = (By.XPATH, "//input[@type='checkbox'][2]")

wait.until(EC.visibility_of_element_located(CHECKBOX_1)).click()
assert driver.find_element(*CHECKBOX_1).get_attribute("checked") is not None, "Чек-бокс не нажат"

wait.until(EC.visibility_of_element_located(CHECKBOX_2)).click()
assert not driver.find_element(*CHECKBOX_2).is_selected(), "Чек-бокс нажат"
