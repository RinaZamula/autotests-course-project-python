import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/tracks")
time.sleep(3)

#Sign in button
driver.find_element(By.XPATH, "//button[contains(@class, '!whitespace-nowrap')]")

#Header
driver.find_element(By.XPATH, "//h1[text()='What do you want to do?']")

#Logo
driver.find_element(By.XPATH, "(//a[@class='nav-link'])[1]")

#Banner
driver.find_element(By.XPATH, "//div[contains(@class, 'banner-discount-timer')]")

#Kotlin Developer Card
driver.find_element(By.XPATH, "//div[@class='card-body']//h5[text()='Kotlin Developer']")
