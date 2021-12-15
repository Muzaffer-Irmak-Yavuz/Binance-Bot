def calculate_sma(closeList : list , count : int):
    sum=0
    for i in range(0,count):
        sum+=float(i)
        print(float(i))

    return int(sum/count)

def calculate_ema(closeList : list):
    sma=calculate_sma(closeList,12)
    ema=closeList[12]*(2/13)+sma*(1-(2/13))
    return ema