import requests
from bs4 import BeautifulSoup
import smtplib

#URL for the product(s) you wish to track
URL = "https://www.amazon.com/gp/product/B00JD4TAWI/ref=ox_sc_saved_title_3?smid=ATVPDKIKX0DER&psc=1"
#Info for the device you are running the program on
#
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15"}
PRICE_VALUE = 160
EMAIL_ADDRESS = "wayne.s.covell@gmail.com"

def trackPrices():
    price = float(getPrice())
    if price > PRICE_VALUE:
        diff = int(price - PRICE_VALUE)
        print(f"Still £{diff} too expensive")
    else:
        print("Cheaper! Notifying...")
        sendEmail()
    pass

def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()[1:4]
    print(title)
    print(price)
    return price

def sendEmail():
    subject = "Amazon Price Dropped!"
    mailtext='Subject:'+subject+'\n\n'+URL

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, 'wazLincsLuna18!')
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
    pass

if __name__ == "__main__":
    trackPrices()