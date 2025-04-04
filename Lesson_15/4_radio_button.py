from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/radio-button")

YES_RADIO_BUTTON = (By.XPATH, "//input[@id='yesRadio']")
YES_RADIO_BUTTON_LABEL = (By.XPATH, "//label[@for='yesRadio']")
NO_RADIO_BUTTON = (By.XPATH, "//input[@id='noRadio']")

wait.until(EC.visibility_of_element_located(YES_RADIO_BUTTON_LABEL)).click()
assert driver.find_element(*YES_RADIO_BUTTON).is_selected(), "Радиокнопка не выбрана"

assert not driver.find_element(*NO_RADIO_BUTTON).is_enabled(), "Кнопка активна"
