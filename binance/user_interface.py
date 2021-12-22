#   @authors : Muzaffer Irmak Yavuz , İlkay Düzgün
#   @title   : Binance Api Wrapper With Telegram Api And AWS Mysql db 


from mysql_wrapper import  mysql_handler
from wrapper import BinanceHandler
import telegramapi as tl
import indicator





Hmysql = mysql_handler()
Hinstance = BinanceHandler()


once = 1

for i in range(33,366):

    values = Hinstance.get_historical_once(symbol="BTCUSDT",interval="1d",utc_time_start="1 Jan, 2020",utc_time_end="1 Jan, 2021",count=i,last=33)

    rsi = indicator.rsi(values)
    macd , macd_s , macd_h = indicator.calculate_macd(values)

    

    print(values[-1]['close'],macd,macd_s,macd_h,rsi)

    continue


    if (macd[i-31] > 0 and once == 1):
        tl.assert_user("Macd turns positive in BTCUSDT")
        once = 0

    if (macd[i-31] < 0 and once == 0):
        tl.assert_user("Macd turns negative in BTCUSDT")
        once = 1

    
   




    