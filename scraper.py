import requests
from bs4 import BeautifulSoup
import smtplib #enables us to send emails
import time

URL = "https://www.flipkart.com/provogue-running-shoes-men/p/itmef95af271c385?pid=SHOFGS3HSNHHGAUA&lid=LSTSHOFGS3HSNHHGAUAS4IDRZ&marketplace=FLIPKART&srno=b_1_5&otracker=clp_omu_Fashion%2BTop%2BDeals_1_2.dealCard.OMU_Fashion%2BTop%2BDeals_offers-store_FIMUD8OREN7I_1&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Fashion%2BTop%2BDeals_NA_dealCard_cc_1_NA_view-all_1&fm=neo%2Fmerchandising&iid=4d2cc88d-ec4d-446d-a2f9-8a771d753309.SHOFGS3HSNHHGAUA.SEARCH&ppt=browse&ppn=browse&ssid=gwejbhzqho8lkydc1595834340333"
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
#search for 'my user agent ' in any browser and you will get the link.

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    #_2J4LW6
    title = soup.find('span', {'class':['_2J4LW6']}).get_text()
    #_1vC4OE _3qQ9m1
    price = soup.find('div', {'class':['_1vC4OE _3qQ9m1']}).get_text()
    converted_price = float(price[1:5])

    if (converted_price < 900):
        send_mail()


    #print(soup.prettify)
    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    #This is how awe establish a connection to google server..
    #the connection number is 587
    server.ehlo()
    #it is a command send by an email server
    #to identify itself when connectinng to another email
    server.starttls()
    #This encrypts our connection
    server.ehlo()

    server.login('sharath.icwai@gmail.com', 'zajhwzyjscbrchyf')
    #We enter our email, password to login and recieve mails.

    subject = 'Price fell down!!!'
    body = 'Check the link https://www.flipkart.com/provogue-running-shoes-men/p/itmef95af271c385?pid=SHOFGS3HSNHHGAUA&lid=LSTSHOFGS3HSNHHGAUAS4IDRZ&marketplace=FLIPKART&srno=b_1_5&otracker=clp_omu_Fashion%2BTop%2BDeals_1_2.dealCard.OMU_Fashion%2BTop%2BDeals_offers-store_FIMUD8OREN7I_1&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Fashion%2BTop%2BDeals_NA_dealCard_cc_1_NA_view-all_1&fm=neo%2Fmerchandising&iid=4d2cc88d-ec4d-446d-a2f9-8a771d753309.SHOFGS3HSNHHGAUA.SEARCH&ppt=browse&ppn=browse&ssid=gwejbhzqho8lkydc1595834340333'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sharath.icwai@gmail.com',
        'sharath.icwai@gmail.com',
         msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

while(True):
    check_price()
    time.sleep(60)
