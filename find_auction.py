import requests
from bs4 import BeautifulSoup

class auctionFinder(object):
    HOME_URL = 'https://auctions.ramco.uk/auctions'

    auction = {}

    client = requests.Session()

    r = client.get(HOME_URL)
    
    soup = BeautifulSoup(r.text, 'lxml')

    auctionListings = soup.find('div', attrs={'class': 'ui divided items auction-list'})

    listing = auctionListings.findAll('div', attrs={'class': 'row'})

    x=0
    for row in listing:
        title = row.find('a', attrs={'class': 'color-inherit'}).get_text()
        link = row.find('a', attrs={'class': 'color-inherit'})['href']
        dates = row.findAll('span', attrs={'class': 'sale-date'})

        auctionLot = {
            'title': title,
            'link':link,
            'start': dates[0].get_text(),
            'end': dates[1].get_text()
        }
        
        auction['lot_'+ str(x)]=auctionLot
        x += 1