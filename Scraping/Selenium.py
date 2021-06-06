from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Seleniumを使用する場合には、ブラウザに対応したWebDriverが必要


url = "https://www.google.com"
keyword = "スクレイピング"

# ヘッドレスモード
options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get(url)

# 3秒後にキーワード検索
time.sleep(3)
search = driver.find_element_by_name("q")
search.send_keys(keyword)
search.submit()

# 検索結果を取得する
soup = BeautifulSoup(driver.page_source, "html.parser")
results = soup.find_all("h3", attrs={"class": "LC20lb"})

for i, result in enumerate(results):
    print("%d: %s " % (i+1, result.get_text()))

# 5秒後に閉じる
time.sleep(5)
driver.quit()
