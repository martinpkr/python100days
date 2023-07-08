from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
chrome_driver_path = '/home/martin.kirilov/Documents/chrome_driver/chromedriver'

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.instagram.com/")

time.sleep(1)
accept_cookies = driver.find_element(By.CSS_SELECTOR,'._a9_0')
accept_cookies.click()

input_username = driver.find_element(By.NAME,'username')
input_pass = driver.find_element(By.NAME,'password')

input_username.send_keys('marthenisvictorious')
input_pass.send_keys('Nikolche69')



