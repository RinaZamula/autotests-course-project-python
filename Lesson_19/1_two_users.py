from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
user_1 = webdriver.Chrome(service=service) #Первый объект вебдрайвера для первого пользователя
wait = WebDriverWait(user_1, 15, poll_frequency=1)

LOGIN_FIELD = (By.XPATH, "//input[@type='email']")
PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

user_1.get("https://hyperskill.org/login")
wait.until(EC.visibility_of_element_located(LOGIN_FIELD)).send_keys("alekseik@ya.ru")
wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys("Qwerty132!")
wait.until(EC.visibility_of_element_located(SUBMIT_BUTTON)).click()

user_2 = webdriver.Chrome(service=service) # инициализируем объект для второго пользователя

# переходим по ссылке, чтобы проверить, что пользователь не залогинен; откроется новая сессия браузера
user_2.get("https://hyperskill.org/login")