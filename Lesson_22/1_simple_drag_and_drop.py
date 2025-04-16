from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)
actions = ActionChains(driver)

driver.get("https://demoqa.com/droppable")

ITEM = (By.XPATH, "//div[@id='draggable']")
TARGET = (By.XPATH, "//div[@id='droppable']")

item = wait.until(EC.visibility_of_element_located(ITEM))
target = wait.until(EC.visibility_of_element_located(TARGET))

actions.drag_and_drop(item, target).pause(3).perform()