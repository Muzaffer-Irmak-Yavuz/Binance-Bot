def calculate_sma(closeList : list):
    sum=0
    for i in closeList:
        sum+=float(i)
        print(float(i))

    return int(sum/10)