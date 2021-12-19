from wrapper import BinanceHandler
import indicator

import pandas as pd



Hinstance = BinanceHandler()

values = Hinstance.get_historical_once(symbol="BTCUSDT",interval="1d",utc_time_start="1 Feb, 2019",utc_time_end="1 Jan, 2021",count=1)


for i in range(600,670):
    values = Hinstance.get_historical_once(symbol="BTCUSDT",interval="1d",utc_time_start="1 Feb, 2019",utc_time_end="1 Jan, 2021",count=i,last=30)

    rsi = indicator.rsi(values)
    macd = indicator.calculate_macd(values)
    mac = macd['macd']
    macs = macd['macd_s']
    mach = macd['macd_h']
    
    
    print("macd :",int(mac[i-31]),"macd_s :",int(macs[i-31]),"macd_h :",int(mach[i-31]),"rsi :",int(rsi[i-31]))
    
   




    