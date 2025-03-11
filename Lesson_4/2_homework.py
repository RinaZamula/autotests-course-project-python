# step 1
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# step 2-3
driver.get("https://www.youtube.com/")
print(driver.title)

# step 4-5
driver.get("https://habr.com/ru/feed/")
print(driver.title)

# step 6
driver.back()
assert driver.current_url == "https://www.youtube.com/", "Ой, мы попали куда-то не туда!"

# step 7-8
driver.refresh()
print(driver.current_url)

# step 9-10
driver.forward()
assert driver.current_url == "https://habr.com/ru/feed/", "Ой, мы снова не там!"
