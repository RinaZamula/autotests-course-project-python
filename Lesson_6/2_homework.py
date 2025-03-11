import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service.service_args)

driver.get("https://testautomationpractice.blogspot.com")
time.sleep(3)

icon = driver.find_element(By.CLASS_NAME, "wikipedia-icon")
print(icon)

field = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
print(field)

button = driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
print(button)

title = driver.find_element(By.TAG_NAME, "h1")
print(title)
time.sleep(3)

