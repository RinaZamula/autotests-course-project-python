import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/upload-download")

upload_file_button = driver.find_element(By.XPATH, "//input[@type='file']")
upload_file_button.send_keys(f"{os.getcwd()}\\downloads\\my-notion-face-transparent.png")

time.sleep(3)
