import requests  # allows for network searches
from bs4 import BeautifulSoup  # webscraper
import smtplib  # mail protocol, allows for emails
import time  # used to interact with real time

# Install requests and bs4 to run code "pip install requests bs4"

URL = "https://www.amazon.com/gp/product/B00JD4TAWI/ref=ox_sc_saved_title_3?smid=ATVPDKIKX0DER&psc=1"

# Search "my user agent" on google.com for info below
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:])

    # Insert desired price point
    if (converted_price < 300.00):
        send_mail()

    print(title.strip())
    print(converted_price)


# Need to go to following site to allow gmail use: https://myaccount.google.com/lesssecureapps
def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()  # extended connection for smtp verification
    server.starttls()  # initiates encrypted connection
    server.ehlo()

    server.login("YOUR_EMAIL", "YOUR_PASSWORD")

    subject = "Price fell down!"
    body = "Check the amazon link: https://www.amazon.com/gp/product/B00JD4TAWI/ref=ox_sc_saved_title_3?smid=ATVPDKIKX0DER&psc=1"

    msg = f"Subject: {subject}\n\n{body}"

    # format: sender, receiver, messsage text
    server.sendmail(
        "SENDER_EMAIL",
        "RECEIVER_EMAIL",
        msg
    )
    print("EMAIL HAS BEEN SENT")

    server.quit()


while True:
    check_price()
    time.sleep(86400) # Amount of time in between price checks
