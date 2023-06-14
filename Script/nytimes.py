import requests
import bs4 as beautifulsoup

client = requests.session()
months = [f"https://www.nytimes.com/sitemap/1972/{i:02}" for i in range(1, 13)]
days = [f"{month}/{i:02}" for i in range(1, 32) for month in months]

# "10 european stylists"
for day in days:
    print(f"Checked: {day}")
    response = client.get(day)
    a_ = beautifulsoup.BeautifulSoup(response.text, "html.parser").select("#site-content > div > ul > li > a")
    for a in a_:
        if "european" in a.text.lower():
            print(a.text, a["href"])
        if "stylist" in a.text.lower():
            print(a.text, a["href"])
        if "10 " in a.text.lower():
            print(a.text, a["href"])