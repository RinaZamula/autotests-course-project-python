import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Для теста использовался бесплатный прокси, в работе их лучше не использовать
PROXY = "178.236.247.252:3128"

options = Options()
options.add_argument(f"--proxy-server={PROXY}")

driver = webdriver.Firefox(options=options)

driver.get("https://2ip.ru")

time.sleep(3)