import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("http://the-internet.herokuapp.com/dropdown")

DROPDOWN_SELECT_SELECTOR = (By.XPATH, "//select[@id='dropdown']")

dropdown = Select(driver.find_element(*DROPDOWN_SELECT_SELECTOR))

#Перебор всех опций
option_list = dropdown.options[1:]

for option in option_list:
    dropdown.select_by_visible_text(option.text)
    time.sleep(2)

for index, option in enumerate(option_list):
    dropdown.select_by_index(index + 1)
    time.sleep(2)

for option in option_list:
    dropdown.select_by_value(option.get_attribute("value"))
    time.sleep(2)