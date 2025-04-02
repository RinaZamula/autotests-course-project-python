from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")

cookies_before = driver.get_cookies()
print(cookies_before)

# Удаляем конкретную куки
driver.delete_cookie("__eoi")

cookies_after = driver.get_cookies()
print(cookies_after)

# удаляем все куки
driver.delete_all_cookies()

cookies_deleted = driver.get_cookies()
print(cookies_deleted)
