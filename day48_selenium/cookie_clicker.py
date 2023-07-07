import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

start_time = time.time()
chrome_driver_path = '/home/martinxnello/Documents/chromedriver'

game_is_on = True

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

products = driver.find_element(By.XPATH,'//*[@id="store"]')
cookie = driver.find_element(By.ID, 'cookie')
all_products = products.find_elements(By.CSS_SELECTOR,'div')
while game_is_on:
    cookie.click()
    money = driver.find_element(By.ID,'money').text
    current_time = time.time()
    elapsed_time = current_time - start_time
    str_elapsed_time = str(elapsed_time)
    int_elapsed_time = int(str_elapsed_time[0])

    if int_elapsed_time % 5 == 0:
        for pr in all_products:
            try:
                price = driver.find_element(By.CSS_SELECTOR,'#store b').text.split(' - ')[1]
                print(price)
                if float(money) >= float(price):
                    driver.find_element(By.CSS_SELECTOR,'#store b').click()

            except IndexError:
                print("no such index")
    if int_elapsed_time == 300:
        print(f'you collected: {money}')





