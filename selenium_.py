from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from json import load
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

service = Service(r"C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

lista = load(open(r"D:\\Python\Python\Variables\Link.json", 'r'))

for i in lista:
    driver.execute_script(f'''window.open("{i}","_blank");''')

driver.switch_to.window(driver.window_handles[0])
driver.close()
while True:
    for i in range(len(lista)):
        driver.switch_to.window(driver.window_handles[i])
        sleep(15)
