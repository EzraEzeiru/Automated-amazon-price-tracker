import bs4
import requests
import smtplib
import os


URL = "https://www.amazon.com/Nintendo-Switch-Lite-Dialga-Palkia/dp/B09CZTD754/ref=sr_1_7?keywords=nintendo+switch&qid=1" \
      "652890273&s=videogames-intl-ship&sprefix=nintendo%2Cvideogames-intl-ship%2C1237&sr=1-7"

MY_EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

headers = {
    "Accept-Language": "en-US,en;q=0.9",

    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    }

response = requests.get(url=URL, headers=headers)
amazon_web_page = response.text

soup = bs4.BeautifulSoup(amazon_web_page, "html.parser")
coded_price = soup.find(name="span", id="priceblock_ourprice")
coded_name = soup.find(name="span", id="productTitle")
product_name = coded_name.getText().strip()
price = float(coded_price.getText().strip("$"))

BUY_PRICE = 300

if price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="ezeiru.ezra@gmail.com",
                            msg=f"Subject: Product Price Alert!!\n\n {product_name} is now ${price}\n{URL}")
