import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com")
time.sleep(5)

driver.get("https://www.youtube.com/watch?v=JRI9ddlNL8Q")
time.sleep(5)

driver.back()
time.sleep(5)

driver.forward()
time.sleep(5)

driver.refresh()
time.sleep(5)
