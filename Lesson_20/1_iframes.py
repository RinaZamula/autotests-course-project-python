from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) #Первый объект вебдрайвера для первого пользователя
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demo.automationtesting.in/Frames.html")

MULTIPLE_IFRAMES_TAB = (By.XPATH, "//a[text()='Iframe with in an Iframe']")
H5_TAG = (By.XPATH, "//h5")
wait.until(EC.visibility_of_element_located(MULTIPLE_IFRAMES_TAB)).click()

# Переключаемся на родительский iframe
driver.switch_to.frame(1)
print(wait.until(EC.visibility_of_element_located(H5_TAG)).text)

# Переключаемся на дочерний iframe
driver.switch_to.frame(0)
print(wait.until(EC.visibility_of_element_located(H5_TAG)).text)

# Переключаемся на родительский iframe
driver.switch_to.parent_frame()
print(wait.until(EC.visibility_of_element_located(H5_TAG)).text)

# Переключаемся на дефолтный контент
driver.switch_to.default_content()
print(wait.until(EC.visibility_of_element_located(MULTIPLE_IFRAMES_TAB)).text)