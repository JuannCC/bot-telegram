from bs4 import BeautifulSoup 
import requests

def al30d_scraping():
    url = requests.get('https://www.cohen.com.ar/Bursatil/Especie/AL30D')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('div', {'class': 'tdCotizEspecie'})
    #format_result = result.text
    result_text = result.text.strip()
    al30d_price = float(result_text.replace('$', '').replace(',', '.'))

    return al30d_price

def al30d_average_daily():
    url = requests.get('https://www.cohen.com.ar/Bursatil/Especie/AL30D')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('div', {'class': 'tdVariacion positivo'})
    #format_result = result.text
    result_text = result.text.strip()
    al30d_price = float(result_text.replace('%', '').replace(',', '.'))

    return al30d_price

#al30d_price = al30d_average_daily()
#print(al30d_price)