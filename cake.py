from bs4 import BeautifulSoup 
import requests

def cake_scraping():
    url = requests.get('https://awebanalysis.com/es/coin-details/pancakeswap/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class': 'text-larger text-price'})
    format_result = result.text

    return format_result

def cake_average_daily():
    url = requests.get('https://awebanalysis.com/es/coin-details/pancakeswap/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('span', {'class': 'cc_neg'})
    format_result = result.text

    return format_result
