from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get("http://44.220.249.251:3001/")

browser.implicitly_wait(0.5)

title_web_nav = browser.find_element(By.CLASS_NAME, "navbar__logo")
title_web = title_web_nav.find_elements(By.TAG_NAME, "h2")



# first_name = browser.find_element(By.ID, "input-firstname")
# last_name = browser.find_element(By.ID, "input-lastname")
# telephone = browser.find_element(By.ID, "input-telephone")
# email = browser.find_element(By.ID, "input-email")
# password = browser.find_element(By.ID, "input-password")
# password_confirm = browser.find_element(By.ID, "input-confirm")
# terms = browser.find_element(By.XPATH, value="//label[@for='input-agree']")
# continue_button = browser.find_element(By.XPATH, value="//input[@value='Continue']")

# first_name.send_keys("FFirstName")
# last_name.send_keys("LLastName")
# email.send_keys("sample-email1@data.com")
# telephone.send_keys("+351999888888")
# password.send_keys("12345678")
# password_confirm.send_keys("12345678")
# terms.click()
# continue_button.click()

print(title_web[0].text)
assert title_web[0].text == "Assignment 3 Ecommerce Jenkins"

browser.get("http://44.220.249.251:3001/signin")
signIn_container = browser.find_elements(By.CLASS_NAME, "innerContainer")
signIn_title = signIn_container[0]
signIn_title = signIn_title.find_elements(By.TAG_NAME, "p")
print(signIn_title)
assert signIn_title.text == "Sign In"