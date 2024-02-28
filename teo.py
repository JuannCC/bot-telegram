from bs4 import BeautifulSoup 
import requests

def teo_scraping():
    url = requests.get('https://www.acciones.com/nyse/stock/teo_telecom-argentina-sa-adr/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('span', {'class': 'cajetillapost__text'})
    result_text = result.text.strip()
    teo_price = float(result_text.replace('$', '').replace(',', '.'))

    return teo_price

'''def teo_average_daily():
    url = requests.get('https://www.acciones.com/nyse/stock/teo_telecom-argentina-sa-adr/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('span', {'class': 'details-box__item__text'})
    #result_text = result.text.strip()
    #teo_price = float(result_text.replace('%', '').replace(',', '.'))

    return result'''

#teo_price = teo_average_daily()
#print(teo_price)