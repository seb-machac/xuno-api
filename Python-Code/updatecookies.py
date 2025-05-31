from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests
import json

options = Options()
options.add_argument("--headless")  # Run in background
driver = webdriver.Chrome(options=options)

driver.get("https://pmsc.xuno.com.au/index.php/login")

driver.find_element(By.NAME, "username").send_keys("MAC0001")
driver.find_element(By.NAME, "password").send_keys("Rat.4918")
driver.find_element(By.XPATH, "//button[text()='Sign-in']").click()

time.sleep(5)  # You could wait for a specific element instead

cookies = driver.get_cookies()

with open("cookies_secret.json", "w") as f:
    json.dump(cookies, f)

driver.quit()
