from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument("--incognito")
options.add_argument("--disable-cache")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--window-size=700,700")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/status_codes")

a_list = driver.find_elements(By.XPATH, "//li/a")

for a in a_list:
    a.click()
    driver.back()
