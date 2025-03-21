import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
preferences = {
    "download.default_directory": f"{os.getcwd()}\\homework_downloads"
}
options.add_experimental_option("prefs", preferences)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/download")

files_to_download = driver.find_elements(By.XPATH, "//div[@class='example']/a")

for file in files_to_download:
    file.click()

# Проверяем, есть ли последний файл в папке, если нет - ждем секунду
while not os.path.exists(f"{os.getcwd()}\\homework_downloads\\Jpeg_with_exif.jpeg"):
    time.sleep(1)
