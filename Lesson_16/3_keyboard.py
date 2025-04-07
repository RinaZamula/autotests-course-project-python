import platform
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("http://the-internet.herokuapp.com/key_presses")

INPUT_SELECTOR = (By.XPATH, "//input[@id='target']")

CTR_CMD = Keys.COMMAND if platform.system() == "Darwin" else Keys.CONTROL

input_field = wait.until(EC.visibility_of_element_located(INPUT_SELECTOR))
input_field.send_keys("AFGDFGDFGDFGDFGDF")
time.sleep(2)
input_field.send_keys(CTR_CMD + "A")
time.sleep(2)
input_field.send_keys(Keys.DELETE)
time.sleep(2)
