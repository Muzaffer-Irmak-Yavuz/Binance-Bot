#   @authors : Muzaffer Irmak Yavuz , İlkay Düzgün
#   @title   : Binance Api Wrapper With Telegram Api And AWS Mysql db 


from wrapper import BinanceHandler
import indicator

import pandas as pd
import telegramapi as tl


Hinstance = BinanceHandler()

once = 1

for i in range(100,366):
    values = Hinstance.get_historical_once(symbol="BTCUSDT",interval="1d",utc_time_start="1 Jan, 2020",utc_time_end="1 Jan, 2021",count=i,last=26)

    rsi = indicator.rsi(values)
    macd = indicator.calculate_macd(values)
    mac = macd['macd']
    macs = macd['macd_s']
    mach = macd['macd_h']
    
    
    print("Index :",i,"Open :",values[i-31]["open"],"macd :" ,int(mac[i-31]),"macd_s :",int(macs[i-31]),"macd_h :",int(mach[i-31]),"rsi :",int(rsi[i-31]))

    if (mac[i-31] > 0 and once == 1):
        tl.assert_user("Macd turns positive in BTCUSDT")
        once = 0

    if (mac[i-31] < 0 and once == 0):
        tl.assert_user("Macd turns negative in BTCUSDT")
        once = 1

    
   




    