#!/usr/bin/env python3
import time
import sys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

chrome_options = Options()
# chrome_options.add_argument('--verbose')
chrome_options.add_argument(r'--user-data-dir="C:\Users\matti\AppData\Local\Google\Chrome\User Data\Profile 4"')
# chrome_options.add_argument(r'--profile-directory=Default')
# chrome_options.add_argument("--headless")
chromedriver_service = Service(r"C:\Program Files (x86)\Chromedriver\chromedriver.exe")
driver = webdriver.Chrome(
    service=chromedriver_service,
    options=chrome_options
)
actions = ActionChains(driver)


class Selectors:
    ...


if __name__ == '__main__':
    # python blocca-selenium.py https://it.quora.com/profile/Silvio-Vergani 20
    if '--help' in sys.argv:
        print('python blocca-selenium.py <user-url> <login-time>')
        exit(0)
    url: str = sys.argv[1]
    driver.get(url)
    login_time = int(sys.argv[2])
    time.sleep(login_time) # Wait for login