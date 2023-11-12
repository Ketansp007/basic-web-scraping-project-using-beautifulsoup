import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
bewkoof = pd.DataFrame()
for i in range(1,3):  # fetching data from bewkoof site for 2 pages
    time.sleep(1)
    url = 'https://www.bewakoof.com/men-printed-tshirts/{}'.format(i)
    reply = requests.get(url).text
    soup = BeautifulSoup(reply,'lxml')
    all = soup.find_all('div',class_='productCardDetail pdt-card-h')
    brand = []
    item_name = []
    discounted_price = []
    actual_price = []
    tribe_price = []
    for item in all:
        brand.append(item.find_all('h3',class_='brand-name undefined')[0].text)
        item_name.append(item.find_all('h2',class_='clr-shade4 h3-p-name undefined false')[0].text)
        discounted_price.append(int(item.find_all('div',class_='discountedPriceText clr-p-black false')[0].text[1:]))
        actual_price.append(int(item.find_all('div',class_='actualPriceText clr-shade5')[0].text[1:]))
        tribe_price.append(int(item.find_all('div',class_='loyaltyPriceBox')[0].text.split()[0][1:-3]))
        col = {'brand':brand,'item_name':item_name,'discounted_price':discounted_price,'actual_price':actual_price,'tribe_price':tribe_price}
        df = pd.DataFrame(col)
        bewkoof = pd.concat([bewkoof,df],ignore_index=True)
        # clear the appended list
        brand.clear()
        item_name.clear()
        discounted_price.clear()
        actual_price.clear()
        tribe_price.clear()

