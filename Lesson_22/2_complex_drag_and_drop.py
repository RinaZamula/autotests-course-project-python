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

driver.get("https://tympanus.net/Development/DragDropInteractions/index.html")

ITEM = (By.XPATH, "(//div[@class='grid__item'])[2]")
TARGET = (By.XPATH, "(//div[@class='drop-area__item'])[3]")

item = wait.until(EC.visibility_of_element_located(ITEM))
target = wait.until(EC.visibility_of_element_located(TARGET))

actions.click_and_hold(item).pause(2).move_to_element(target).pause(2).release().pause(2).perform()