from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/alerts")

#Алерт с кнопкой ОК
BUTTON_1 = (By.XPATH, "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()
alert_1 = wait.until(EC.alert_is_present())

driver.switch_to.alert
alert_1.accept()

#Алерт с кнопкой ОК, но его появления надо ждать 5 секунд
BUTTON_2 = (By.XPATH, "//button[@id='timerAlertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_2)).click()
alert_2 = wait.until(EC.alert_is_present())

driver.switch_to.alert
alert_2.accept()

#Алерт с кнопкой ОК и ОТМЕНА
BUTTON_3 = (By.XPATH, "//button[@id='confirmButton']")
wait.until(EC.element_to_be_clickable(BUTTON_3)).click()
alert_3 = wait.until(EC.alert_is_present())

driver.switch_to.alert
alert_3.dismiss()

#Алерт с полем ввода
BUTTON_4 = (By.XPATH, "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()
alert_4 = wait.until(EC.alert_is_present())

driver.switch_to.alert
print(alert_4.text)
alert_4.send_keys("Мой текст")
alert_4.accept()
