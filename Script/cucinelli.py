import sys
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import bs4 as beautifulsoup


chrome_options = Options()
# chrome_options.add_argument("--headless")
service = Service(
    executable_path=r"C:\Users\vegans\Downloads\chromedriver_win32\chromedriver.exe",
)
driver = webdriver.Chrome(service=service, options=chrome_options)
client = requests.session()


class Xpaths:
    accept_button = "/html/body/div[6]/div[2]/div/div/div[2]/div/div/button"
    colors_ = "/html/body/div[1]/div[4]/div[3]/div[1]/section[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/div/button/span[2]"
    description_ = "/html/body/div[1]/div[4]/div[3]/div[1]/section[1]/div[4]/div/div/div[1]/div/div[1]/div/p"
    details_ = "/html/body/div[1]/div[4]/div[3]/div[1]/section[1]/div[4]/div/div/div[3]/div/div[1]/div/p[1]"
    sizes_ = "/html/body/div[1]/div[4]/div[3]/div[1]/section[1]/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/div[1]/div[2]/div[3]/div/button/span"
    # s__ = "/html/body/div[1]/div[4]/div[3]/div[1]/section[1]/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/div[1]/div[2]"

class CssSelectors:
    colors_ = "#maincontent > div.product-detail.cc-pdp > div.cc-container-full.js-open-requestsize-from-plp > section.cc-pdp__wrp > div.cc-pdp__info > div > div.cc-pdp__info__focus > div.cc-pdp__content-attributes > div > div.cc-attribute.cc-attribute--color > div.cc-content-colors-choice > div > div > button > span.cc-color-text.js-color-text"
    name_ = "#maincontent > div.product-detail.cc-pdp > div.cc-container-full.js-open-requestsize-from-plp > section.cc-pdp__wrp > div.cc-pdp__info > div > div.cc-pdp__info__focus > div.cc-pdp__content-title > h1"
    details_expander = "#maincontent > div.product-detail.cc-pdp > div.cc-container-full.js-open-requestsize-from-plp > section.cc-pdp__wrp > div.cc-pdp__details > div > div > div.cc-pdp__accordion__col.cc-pdp__accordion__col--3 > div > button"
    details_ = "#pdpAccordion3 > div > p:nth-child(1)"
    composition_ = "#pdpAccordion3 > div > p:nth-child(2)"
    sizes_expander = "#maincontent > div.product-detail.cc-pdp > div.cc-container-full.js-open-requestsize-from-plp > section.cc-pdp__wrp > div.cc-pdp__info > div > div.cc-pdp__info__focus > div.cc-pdp__content-attributes > div > div.cc-attribute.cc-attribute--size > div.cc-content-size-choice > button"
    sizes_ = "#size-overlay > div.cc-size-choice-overlay-container.cc-modal.js-selectSize > div.cc-size-list.js-upload-size > div > span"
    price_ = "span.cc-price-text"
    colors_button = "#maincontent > div.product-detail.cc-pdp > div.cc-container-full.js-open-requestsize-from-plp > section.cc-pdp__wrp > div.cc-pdp__info > div > div.cc-pdp__info__focus > div.cc-pdp__content-attributes > div > div.cc-attribute.cc-attribute--color > div.cc-content-colors-choice > div > div.cc-item > button"
    image_ = "#pdpImages-{} > div:nth-child(1) > picture > img"
    image_sobstitute = "div.cc-image-list.js-image-list.cc-pdp__image-list > div:nth-child(1) > picture > img"
    sizes_closer = "#size-overlay > div.cc-size-choice-overlay-container.cc-modal.js-selectSize > div.cc-overlay-head.cc-modal-header > button > svg > use"
    product_id_ = "#maincontent > div.product-detail.cc-pdp > div.cc-container-full.js-open-requestsize-from-plp > section.cc-pdp__wrp > div.cc-pdp__info > div > div.cc-pdp__info__focus > span"

if __name__ == "__main__":
    driver.get(sys.argv[1])
    data: dict[str, str | dict[str, str]] = {}
    data["url"] = sys.argv[1]
    data["type"] = data["url"].split("/")[-2]
    data["category"] = data["url"].split("/")[-4]
    product_id = driver.find_element(By.CSS_SELECTOR, CssSelectors.product_id_).text.split(" ")[-1]

    time.sleep(0.5)
    try:
        button = driver.find_element(By.XPATH, Xpaths.accept_button)
        button.click()
        time.sleep(0.8)
    except:
        pass

    colors_ = driver.find_elements(By.CSS_SELECTOR, CssSelectors.colors_)
    data["color"]: str = ""
    if len(colors_) > 2:
        for color_ in colors_:
            data["color"] += color_.text.split("(")[0].strip() + ", "
            if color_ == colors_[-2]:
                data["color"] = data["color"].removesuffix(", ") + " e "
            if color_ == colors_[-1]:
                data["color"].removesuffix(", ")
    elif len(colors_) == 2:
        data["color"] = colors_[0].text.split("(")[0].strip() + " e " + colors_[1].text.split("(")[0].strip()
    else:
        data["color"] = colors_[0].text.split("(")[0].strip()
    data["color"] = data["color"].lower()
    data["name"] = driver.find_element(By.CSS_SELECTOR, CssSelectors.name_).text
    try:
        data["description"] = driver.find_element(By.XPATH, Xpaths.description_).text
    except:
        pass

    soup = beautifulsoup.BeautifulSoup(
        client.get(
            data["url"]
        ).text,
        "html.parser"
    )
    try:
        data["details"] = "- " + soup.select_one(CssSelectors.details_).text.replace("\n", "\n- ").strip()
        data["details"] += "\n- Composizione: " + soup.select_one(CssSelectors.composition_).text.strip()
    except:
        pass

    driver.find_element(By.CSS_SELECTOR, CssSelectors.sizes_expander).click()
    time.sleep(0.5)
    sizes_temp = driver.find_elements(By.XPATH, Xpaths.sizes_)
    data["sizes"] = ""
    for index in range(len(sizes_temp)):
        if (index % 3 == 0):
            data["sizes"] += f"{sizes_temp[index].text.strip()}, "
    data["sizes"] = data["sizes"].removesuffix(", ").replace("½", ".5")
    data["price"] = soup.select_one(CssSelectors.price_).text.split(",")[0].removeprefix("€ ")
    data["images"]: list[dict[str, str]] = []
    driver.find_element(By.CSS_SELECTOR, CssSelectors.sizes_closer).click()
    time.sleep(0.5)
    try:
        for button_ in driver.find_elements(By.CSS_SELECTOR, CssSelectors.colors_button):
            button_.click()
            time.sleep(0.5)
            try:
                src = driver.find_element(By.CSS_SELECTOR, CssSelectors.image_.format(product_id)).get_attribute("src")
            except:
                src = driver.find_element(By.CSS_SELECTOR, CssSelectors.image_sobstitute).get_attribute("src")
            color = driver.find_element(By.CSS_SELECTOR, CssSelectors.colors_).text.split("(")[0].strip().lower()
            # data["images"].append({color: f"https://shop.brunellocucinelli.com{src}"})
            data["images"].append({"color": color, "url": src})
            # driver.navigate().refresh()
            driver.get(sys.argv[1])
            time.sleep(0.5)
    except:
        pass

    file = open(f"products/{product_id}.txt", "w")
    for key, value in data.items():
        print(key.upper())
        print(value)
        print(key.upper(), file=file)
        print(value, file=file)