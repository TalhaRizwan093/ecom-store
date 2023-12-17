from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get("http://44.213.60.56:3001/")

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

browser.get("http://44.213.60.56:3001/signin")
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
# submit = browser.find_element(By.TYPE, "submit")
# print(submit)
# submit.click()
alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
alert_text = alert.text
print(alert_text)
assert alert_text == "Sucessfully account opened "
alert.accept()
browser.get("http://44.213.60.56:3001/signin")
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
print(nav_links_logout_text.get_attribute("innerHTML"))
print("logout", nav_links_logout_text)

