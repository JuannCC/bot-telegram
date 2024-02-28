from bs4 import BeautifulSoup
import requests
import schedule
from al30 import al30d_scraping, al30d_average_daily
from btc import btc_scraping, btc_average_daily
from cake import cake_scraping, cake_average_daily
from teo import teo_scraping
from disn import dis_scraping

#Envia el resultado al Telegram
def bot_send_text(bot_message):
    
    bot_token = 'colocar el token'
    bot_chatID = 'colocar ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    ###comprobacion de errores
    if response.status_code == 200:
     print("Mensaje enviado con éxito")
    else:
       print("Error al enviar el mensaje")
    print(response.text)
    return response
    ###

#test_bot = bot_send_text('¡Hola, Telegram!')

#Juntamos la dos funciones anteriores para enviar el precio
def report():
    btc_price = f'Bitcoin : {btc_scraping()} --> {btc_average_daily()}'
    cake_price = f'Cake : {cake_scraping()} --> {cake_average_daily()}'
    al30d_price = f'AL30D : ${al30d_scraping()} --> {al30d_average_daily()}'
    teo_price = f'TEO : ${teo_scraping()} '
    dis_price = f'DIS : ${dis_scraping()} '
    bot_send_text(btc_price)
    bot_send_text(cake_price)
    bot_send_text(al30d_price)
    bot_send_text(teo_price)
    bot_send_text(dis_price)
    bot_send_text('---------------------------------------------------------')
    return btc_price,cake_price,al30d_price

#btc_price=report()
#test_bot = bot_send_text(btc_price)
if __name__ == '__main__':
    btc_price_report = report()

#Programa un schedule para enviar el resultado a una hora exacta
"""if __name__ == '__main__':

    schedule.every().day.at("09:00").do(report)

    while True:
        schedule.run_pending()"""
