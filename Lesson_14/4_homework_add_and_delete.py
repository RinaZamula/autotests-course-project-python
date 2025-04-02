from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")

driver.add_cookie({
    "name": "username",
    "value": "user123"
})

driver.refresh()

username_cookie = driver.get_cookie("username")

assert username_cookie.keys() is not None, "Something went wrong, Cookie is absent"

if username_cookie.keys() is not None:
    print(username_cookie["value"])

driver.delete_cookie("username")

driver.refresh()

cookie_after_delete = driver.get_cookie("username")

assert cookie_after_delete is None, "Cookie was not deleted"

if cookie_after_delete is not None:
    print(cookie_after_delete["value"])
