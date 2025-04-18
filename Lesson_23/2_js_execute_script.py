import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)
actions = ActionChains(driver)
scrolls = Scrolls(driver, actions)

driver.get("https://seiyria.com/bootstrap-slider/")

EXAMPLE_3_LOCATOR = (By.XPATH, "//h3[text()='Example 3: ']")
example_3_title = wait.until(EC.visibility_of_element_located(EXAMPLE_3_LOCATOR))

scrolls.scroll_to_element(example_3_title)

time.sleep(3)
