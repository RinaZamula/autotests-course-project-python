from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)
actions = ActionChains(driver)

driver.get("https://testkru.com/Elements/Buttons")

LEFT_CLICK_BUTTON = (By.XPATH, "//button[text()='Left click on me']")
DOUBLE_CLICK_BUTTON = (By.XPATH, "//button[text()='Double click on me']")
RIGHT_BUTTON = (By.XPATH, "//button[text()='Right click on me']")
HOVER_CLICK_BUTTON = (By.XPATH, "//button[text()='Hover on me']")

left_click_web_element = wait.until(EC.visibility_of_element_located(LEFT_CLICK_BUTTON))
double_click_web_element = wait.until(EC.visibility_of_element_located(DOUBLE_CLICK_BUTTON))
right_click_web_element = wait.until(EC.visibility_of_element_located(RIGHT_BUTTON))
hover_click_web_element = wait.until(EC.visibility_of_element_located(HOVER_CLICK_BUTTON))

(actions.click(left_click_web_element).pause(3).double_click(double_click_web_element).pause(3)
 .move_to_element(hover_click_web_element).pause(3).context_click(right_click_web_element).pause(3).perform())

assert left_click_web_element.text == "I was left-clicked!", "Left click wasn't performed"
assert double_click_web_element.text == "I was double-clicked!", "Double click wasn't performed"
assert right_click_web_element.text == "I was right-clicked!", "Right click wasn't performed"