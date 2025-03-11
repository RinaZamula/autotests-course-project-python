import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com/")
time.sleep(3)

print(driver.current_url)
print(driver.title)

with open("C:/Users/mzamu/Desktop/1.txt", encoding="UTF-8", mode="w") as file:
    file.write(driver.page_source)

time.sleep(3)