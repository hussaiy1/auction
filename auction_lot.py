from find_auction import auctionFinder
import requests
from bs4 import BeautifulSoup


class auctionLot(object):
    findAuction = auctionFinder()
    auction = findAuction.auction

    DOMAIN = 'https://auctions.ramco.uk'

    choiceString = 'Choose Auction Room: \n'

    for i in range(len(auction)):
        choiceString += str(i) +'. ' + str(auction['lot_' + str(i)]['title']) + '\n' + 'Ending: ' + str(auction['lot_' + str(i)]['end']) + '\n'
    
    choice = int(input(choiceString))


    client = requests.Session()

    url = DOMAIN + str(auction['lot_' + str(choice)]['link'] + '?page=1&pageSize=600000')
    
    r = client.get(url)

    soup = BeautifulSoup(r.text,'lxml')

    lotGrid = soup.find('div', attrs={'class': 'twelve wide column'})
    listing = lotGrid.findAll('div', attrs={'class': 'ui cards'})

    x=1
    for lot in listing:
        title = lot.find('a', attrs={'name': 'lot-title'}).get_text()
        bid = lot.find('span', attrs={'class': 'current-bid-value'}).get_text()
        with open('data.csv', 'a') as f:
            f.write('{}|{}|{} \n'.format(x,title, bid))
        x+=1

