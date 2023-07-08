from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = '/home/martinxnello/Documents/chromedriver'

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

name_input = driver.find_element(By.NAME,'fName')
lname_input = driver.find_element(By.NAME,'lName')
email_input = driver.find_element(By.NAME, 'email')
submit_btn = driver.find_element(By.XPATH,'/html/body/form/button')
name_input.send_keys('kokoshkachan')
lname_input.send_keys('narutokun')
email_input.send_keys('kukuchan@abv.bg')
time.sleep(2)
submit_btn.send_keys(Keys.ENTER)


