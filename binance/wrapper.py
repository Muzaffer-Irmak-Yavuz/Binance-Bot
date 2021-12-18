import binanceApi as pw
from binance.client import Client

class BinanceHandler:
    client  = None
    

    def __init__(self):
        self.client = Client(pw.api_key , pw.secret_key)

    
    def get_historical_once(self, symbol : str ,interval : str,utc_time_start : str , count : int, utc_time_end = None ):
        
        priceDict = {}
        dictList = []
        a_dict = {}

        klines = self.client.get_historical_klines(symbol, interval, utc_time_start, end_str=utc_time_end)

        for i in range(0,count):
            priceDict["open"]  = str(klines[i][1])
            priceDict["high"]  = str(klines[i][2])
            priceDict["low"]   = str(klines[i][3])
            priceDict["close"] = str(klines[i][4])

            a_dict = priceDict.copy()
            dictList.append(a_dict)

        return dictList
