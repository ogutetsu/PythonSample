from selenium import webdriver
import time

username = "ユーザー名"
password = "パスワード"

url = "https://twitter.com/login"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

username_from = driver.find_element_by_name("session[username_or_email]")
password_from = driver.find_element_by_name("session[password]")
username_from.send_keys(username)
password_from.send_keys(password)

password_from.submit()

time.sleep(5)
driver.quit()