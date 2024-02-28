#Obtiene el precio de btc de una web

from bs4 import BeautifulSoup 
import requests

def btc_scraping():
    url = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class': 'text-larger text-price'})
    format_result = result.text

    return format_result

def btc_average_daily():
    url = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('span', {'class': 'cc_pos'})
    format_result = result.text

    return format_result

#teo_price = btc_average_daily()
#print(teo_price)