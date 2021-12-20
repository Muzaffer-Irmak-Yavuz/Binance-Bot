import pandas as pd
from pandas.core import series
import pandas_ta as pta

def calculate_macd(values):
    
    df = pd.DataFrame(values, columns=['close'])

    k = df['close'].ewm(span=12, adjust=False, min_periods=12).mean()
    # Get the 12-day EMA of the closing price
    d = df['close'].ewm(span=26, adjust=False, min_periods=26).mean()
    # Subtract the 26-day EMA from the 12-Day EMA to get the MACD
    macd = k - d
    # Get the 9-Day EMA of the MACD for the Trigger line
    macd_s = macd.ewm(span=9, adjust=False, min_periods=9).mean()
    # Calculate the difference between the MACD - Trigger for the Convergence/Divergence value
    macd_h = macd - macd_s
    # Add all of our new values for the MACD to the dataframe
    
    df['macd'] = df.index.map(macd)
    df['macd_h'] = df.index.map(macd_h)
    df['macd_s'] = df.index.map(macd_s)

    
    
    
        
    return df 
    

def rsi(values, periods = 14, ema = True):

    df = pd.DataFrame(values, columns=['close'])

    df['close'] = pd.to_numeric(df['close'], errors='coerce').fillna(0).astype(int)

    return pta.rsi(df['close'], length = 14)

