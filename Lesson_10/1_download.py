import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
preferences = {
    "download.default_directory": f"{os.getcwd()}\\downloads"
}
options.add_experimental_option("prefs", preferences)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/download")

files_to_download = driver.find_elements(By.XPATH, "//a")
files_to_download[4].click()

time.sleep(3)
