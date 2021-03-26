import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--headless')  # 无头模式

browser = webdriver.Chrome(options=chrome_options)

time.sleep(5)

browser.get("https://www.baidu.com")
print(browser.title)
browser.close()
