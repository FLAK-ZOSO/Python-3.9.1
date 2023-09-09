#!/usr/bin/env python3
import time
import sys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = WebDriver(
    executable_path=r"C:\Program Files (x86)\Chromedriver\chromedriver.exe",
    options=chrome_options
)
actions = ActionChains(driver)


class Selectors:
    upvoters_shower = '//*[@id="mainContent"]/div/div[1]/div/div[5]/div/span/span[4]/div'
    upvoters_counter = '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div'
    upvoters_parent = '//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div'
    upvoters_elements = f"{upvoters_parent}/div"


if __name__ == '__main__':
    # python upvoterDumper.py https://it.quora.com/Come-fare-in-modo-che-gli-immigrati-non-sbarchino-in-Italia/answer/Silvio-Vergani
    if '--help' in sys.argv:
        print('python upvoterDumper.py <url>')
        exit(0)
    url: str = sys.argv[1]
    driver.get(url)
    time.sleep(1)

    # Click to show upvoters
    upvoters_shower = driver.find_element(By.XPATH, Selectors.upvoters_shower)
    upvoters_shower.click()
    time.sleep(1)

    # Get upvoters number
    upvoters_number = int(driver.find_element(By.XPATH, Selectors.upvoters_counter).text.split(' ')[0])

    # Parent of all upvoters
    upvoters_parent = driver.find_element(By.XPATH, Selectors.upvoters_parent)

    upvoters_elements = upvoters_parent.find_elements(By.XPATH, Selectors.upvoters_elements)
    while len(upvoters_elements) < upvoters_number:
        actions.move_to_element(upvoters_elements[-1]).perform()
        time.sleep(1)
        upvoters_elements = upvoters_parent.find_elements(By.XPATH, Selectors.upvoters_elements)

    for upvoter in upvoters_elements:
        url = upvoter.find_elements(By.TAG_NAME, 'a')[0].get_attribute('href')
        print(url)