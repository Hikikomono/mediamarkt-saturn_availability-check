'''
Checkt Verfügbarkeit von einem Produkt im Mediamarkt & Saturn Online Store (AT)
Eingabeparameter: URL des Produkts, eg: "https://www.saturn.at/de/product/_apple-macbook-pro-16"
'''

from bs4 import BeautifulSoup
import requests
from datetime import datetime

#TODO Ausnahmen chekcen / abfangen
def checkAvailability(URL: str):
    response = requests.get(str(URL))
    page_content = response.content
    soup = BeautifulSoup(page_content, "html.parser")
    date_today = datetime.now()
    availability = str(soup.find(property="og:availability"))
    product_name = str(soup.title).strip("<title>").strip("</title>").strip("online kaufen | MediaMark")\
        .strip("online kaufen | SATURN")

    print("Bezeichnung:", product_name)
    if availability.find("nicht") != -1:  # add: -1 = substring nicht enthalten
        print("Produkt NICHT Verfügbar   |  Date:", date_today) #vlt produktname nicht verfügbar printen TODO
    else:
        print("Produkt YAY Verfügbar   |  Date:", date_today) #vlt produktname nicht verfügbar printen TODO

#TESTING
print("-------Mediamarkt-------")
checkAvailability("https://www.mediamarkt.at/de/product/_apple-macbook-pro-16-zoll-mit-touch-bar-space-grau-mvvj2d-a-1761193.html")
print()
checkAvailability("https://www.mediamarkt.at/de/product/_apple-macbook-pro-16-zoll-mit-touch-bar-silber-mvvl2d-a-1761192.html")

print("\n-------Saturn-------")
checkAvailability("https://www.saturn.at/de/product/_apple-macbook-pro-16-zoll-mit-touch-bar-silber-mvvm2d-a-1761186.html")
print()
checkAvailability("https://www.saturn.at/de/product/_apple-macbook-pro-16-zoll-mit-touch-bar-space-grau-mvvj2d-a-1761193.html")