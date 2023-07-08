from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_driver_path = '/home/martinxnello/Documents/chromedriver'

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

get_div = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
print(get_div.text)

driver.quit()