from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_driver_path = '/home/martinxnello/Documents/chromedriver'

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.python.org")
elements = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li time')
names = [el.text for el in driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')]
timedates = [el.text for el in elements]

print(names)
dict = {names.index(name): {} for name in names}
i = 0
for key,value in dict.items():
    print(timedates[i])

    dict[key] = {'time': timedates[i],'name': names[i]}
    i += 1



print(dict)
driver.close()



