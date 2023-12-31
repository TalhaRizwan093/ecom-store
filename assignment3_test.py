from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time 


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

time.sleep(10)

browser.get("http://18.207.136.96:3001")

browser.implicitly_wait(0.5)

title_web_nav = browser.find_element(By.CLASS_NAME, "navbar__logo")
title_web = title_web_nav.find_elements(By.TAG_NAME, "h2")

print(title_web[0].text)
assert title_web[0].text == "Assignment 3 Ecommerce Jenkins"

browser.get("http://18.207.136.96:3001/signin")
signIn_container = browser.find_elements(By.CLASS_NAME, "innerContainer")
signIn_title = signIn_container[0]
signIn_title = signIn_title.find_elements(By.TAG_NAME, "p")
print(signIn_title)
assert signIn_title[0].text == "Sign In"
signUp_button = browser.find_element(By.XPATH, value="//a[@href='/signup']")
signUp_button.click()
signUp_container = browser.find_elements(By.CLASS_NAME, "innerContainer")
signUp_title = signUp_container[0]
signUp_title = signUp_title.find_elements(By.TAG_NAME, "p")
print(signUp_title)
assert signUp_title[0].text == "Signup"

first_name = browser.find_element(By.ID, "fname")
first_name.send_keys("Talha Rizwan")
email = browser.find_element(By.NAME, "email")
email.send_keys("talha@gmail.com")
password = browser.find_element(By.NAME, "password")
password.send_keys("abc123")
print(password)
input_container = browser.find_element(By.CLASS_NAME, "innerContainer")
inputs = input_container.find_elements(By.TAG_NAME, "input")
submit_input = inputs[3]
submit_input.click()
print(submit_input)

alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
alert_text = alert.text
print(alert_text)
assert alert_text == "Sucessfully account opened "
alert.accept()
browser.get("http://18.207.136.96:3001/signin")
signIn_container = browser.find_elements(By.CLASS_NAME, "innerContainer")
signIn_title = signIn_container[0]
signIn_title = signIn_title.find_elements(By.TAG_NAME, "p")
print(signIn_title)
email_signin = browser.find_element(By.NAME, "email")
email_signin.send_keys("talha@gmail.com")
password_signin = browser.find_element(By.NAME, "password")
password_signin.send_keys("abc123")
input_container = browser.find_element(By.CLASS_NAME, "innerContainer")
inputs = input_container.find_elements(By.TAG_NAME, "input")
submit_input = inputs[2]
submit_input.click()
browser.implicitly_wait(2)
nav_links = browser.find_element(By.CLASS_NAME, "navbar__links")
nav_links_logout_li = nav_links.find_elements(By.TAG_NAME, "li")
print(nav_links_logout_li)
nav_links_logout = nav_links_logout_li[2]
print(nav_links_logout)
nav_links_logout_text = nav_links_logout.find_element(By.TAG_NAME, "p")
logout_text = nav_links_logout_text.get_attribute("innerHTML")
assert logout_text == "Logout"
print(nav_links_logout_text.get_attribute("innerHTML"))
print("logout", nav_links_logout_text)

