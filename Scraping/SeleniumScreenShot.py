from selenium import webdriver
import time


url = "https://www.google.com"
keyword = "スクレイピング"

driver = webdriver.Chrome()
driver.get(url)

width = driver.execute_script("return document.body.scrollWidth")
height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(width, height)

time.sleep(3)
driver.save_screenshot("IOFiles/screenshot.png")

time.sleep(3)
driver.quit()