import pickle
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
options.page_load_strategy = "eager"
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://nl.aliexpress.com/item/1005005854085486.html")

BUTTON_ADD_TO_CART = (By.XPATH, "//button/span[text()='Добавьте в корзину']")
wait.until(EC.element_to_be_clickable(BUTTON_ADD_TO_CART)).click()

driver.get("https://www.aliexpress.com/p/shoppingcart/index.html")

with open(os.getcwd() + "\\cookies\\homework_cookies.pkl", "wb") as file:
    pickle.dump(driver.get_cookies(), file)

driver.delete_all_cookies()
driver.refresh()

with open(os.getcwd() + "\\cookies\\homework_cookies.pkl", "rb") as readed_file:
    read_cookies = pickle.load(readed_file)

for cookie in read_cookies:
    driver.add_cookie(cookie)

driver.refresh()
