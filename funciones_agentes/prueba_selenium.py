from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")  

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
sleep(2)

driver.get("https://hybridge.education")
sleep(2)

driver.get("https://openai.com")
sleep(2)


