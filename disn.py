from bs4 import BeautifulSoup 
import requests

def dis_scraping():
    url = requests.get('https://capital.com/es/walt-disney-precio-por-accion')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('b', {'class': 'h2 sharesNameVal__price js-price-sell'})
    result_text = result.text.strip()
    dis_price = float(result_text.replace('$', '').replace(',', '.'))

    return dis_price

'''def dis_average_daily():
    url = requests.get('https://capital.com/es/walt-disney-precio-por-accion')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('div', {'class': 'clrPositive'})
    #result_text = result.text.strip()
    #dis_price = float(result_text.replace('%', '').replace(',', '.'))

    return result'''

#dis_price = dis_average_daily()
#print(dis_price)