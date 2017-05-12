import requests
from bs4 import BeautifulSoup

def trade_spider(max_items):
    items = 0
    while items <= max_items:
        # url = "http://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw=iphone+7+plus&_pgn=" + str(page) + "&rt=nc"
        url = "http://sfbay.craigslist.org/search/eby/sss?s=" + str(items) + "&query=iphone+7&sort=rel"
        print(url)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'hdrlnk'}):
            # href = "https://wong.org" + link.get('href')
            href = "http://sfbay.craigslist.org" + link.get('href')
            title = link.string
            # print(href)
            # print(title)
            get_single_item_data(href)
        items += 100

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('meta', {'name': 'description'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)


trade_spider(100)




# http://sfbay.craigslist.org/search/eby/sss?s=0&query=iphone+7&sort=rel
# http://sfbay.craigslist.org/search/eby/sss?s=100&query=iphone%207&sort=rel
# http://sfbay.craigslist.org/search/eby/sss?s=200&query=iphone%207&sort=rel