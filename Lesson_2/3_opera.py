from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:/Users/mzamu/AppData/Local/Programs/Opera/opera.exe"

service = Service(executable_path=ChromeDriverManager(driver_version="132.0.6834.209").install())
driver = webdriver.Chrome(service=service, options=options)