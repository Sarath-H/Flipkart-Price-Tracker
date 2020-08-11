import requests
from bs4 import BeautifulSoup

URL = "https://www.flipkart.com/provogue-running-shoes-men/p/itmef95af271c385?pid=SHOFGS3HSNHHGAUA&lid=LSTSHOFGS3HSNHHGAUAS4IDRZ&marketplace=FLIPKART&srno=b_1_5&otracker=clp_omu_Fashion%2BTop%2BDeals_1_2.dealCard.OMU_Fashion%2BTop%2BDeals_offers-store_FIMUD8OREN7I_1&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Fashion%2BTop%2BDeals_NA_dealCard_cc_1_NA_view-all_1&fm=neo%2Fmerchandising&iid=4d2cc88d-ec4d-446d-a2f9-8a771d753309.SHOFGS3HSNHHGAUA.SEARCH&ppt=browse&ppn=browse&ssid=gwejbhzqho8lkydc1595834340333"
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
#search for 'my user agent ' in any browser and you will get the link.


page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify)