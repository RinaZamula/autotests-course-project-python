from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")

# Берем все куки для последующего сравнения
cookies_before = driver.get_cookies()
print(cookies_before)

# Добавляем куки
driver.add_cookie({
    "name": "My_Test_Cookie",
    "value": "cookie"
})

# Еще раз берем куки
cookies_after = driver.get_cookies()
print(cookies_after)

# Берем конкретную куки
print(driver.get_cookie("My_Test_Cookie"))
