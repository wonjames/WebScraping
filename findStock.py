import gspread
import datetime
import time
from time import sleep

gc = gspread.oauth()
sh = gc.open("industries_top_100")
list_worksheets = sh.worksheets()
ticker = input("Enter Ticker: ")

for wks in list_worksheets:
    tickerArray = wks.col_values(2)
    for idx, name in enumerate(tickerArray):
        if name == ticker:
            print("Industry: ", wks.title)
            avgChange = wks.acell('C102').value
            avgChangeSplit = avgChange.split('%')[0]
            avgPE = wks.acell('C103').value
            avgVol = wks.acell('C104').value
            avgVolSplit = avgVol.replace(",", "")

            value_list = wks.row_values(idx+1)

            tickerPrice = value_list[2]
            tickerChange = value_list[3]
            tickerVol = value_list[4]
            tickerPE = value_list[5]

            
            s1 = tickerChange.split('%')[0]
            tickerChangeSplit = 0
            if "+" in s1:
                tickerChangeSplit = s1.split("+")[1]
            elif "-" in s1:
                tickerChangeSplit = s1.split("-")[1]
            tickerVolSplit = 0
            if "M" in tickerVol:
                s1 = tickerVol.split('M')[0]
                tickerVolSplit += float(s1)*1000000

            if float(avgChangeSplit) >= float(tickerChangeSplit):
                print("Industry average daily change is greater than or equal to " + ticker)
                print("Industry average: "+avgChange+"\n"+ticker+ " average: " + tickerChange)
            else:
                print("Industry average daily change is lower than " + ticker)
                print("Industry average: "+avgChange+"\n"+ticker+ " average: " + tickerChange)
            if float(avgPE) >= float(tickerPE):
                print("Industry average PE ratio is greater than or equal to " + ticker)
                print("Industry average: "+avgPE+"\n"+ticker+ " PE ratio: " + tickerPE)
            else:
                print("Industry average PE ratio is lower than " + ticker)
                print("Industry average: "+avgPE+"\n"+ticker+ " PE ratio: " + tickerPE)
            if float(avgVolSplit) >= float(tickerVolSplit):
                print("Industry average volume (3 mo) is greater than or equal to " + ticker)
                print("Industry average: "+avgVol+"\n"+ticker+ " average volume (3 mo): " + tickerVol)
            else:
                print("Industry average voloume (3 mo) is lower than " + ticker)
                print("Industry average: "+avgVol+"\n"+ticker+ " average volume (3 mo): " + tickerVol)
            break
    else:
        continue
    break
