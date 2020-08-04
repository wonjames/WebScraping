import requests 
from bs4 import BeautifulSoup 
import gspread
import datetime
import time
from time import sleep
  
gc = gspread.oauth()
sh = gc.open("industries_top_100")
work_sheet = None

def scrap(newUrl, sector):
    url = newUrl
    #open with GET method 
    resp = requests.get(url) 

    #http_respone 200 means OK status 
    if resp.status_code==200: 
        print(sector, "Sector:") 
        # we need a parser,Python built-in HTML parser is enough . 
        soup = BeautifulSoup(resp.text,'html.parser')     
        l = soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')
        total = 0
        peTotal = 0
        avgVolume = 0
        count = 0

        list_worksheets = sh.worksheets()
        check = False
        for wks in list_worksheets:
            if wks.title == sector:
                check = True
                work_sheet = sh.worksheet(sector)
                break
        
        if check == False:
            work_sheet = sh.add_worksheet(title=sector, rows=110, cols=15)

        work_sheet.format('A1:F1', {    
            "backgroundColor": {
            "red": 1.0,
            "green": 1.0,
            "blue": 1.0
            },
            "horizontalAlignment": "CENTER",
            "textFormat": {
            "foregroundColor": {
                "red": 0.0,
                "green": 0.0,
                "blue": 0.0
            },
            "fontSize": 12,
            "bold": True
            }
            })
        date = time.strftime("%m/%d/%Y")
        work_sheet.update('A1', date)
        work_sheet.update('B1', "Ticker")
        work_sheet.update('C1', "Price")
        work_sheet.update('D1', "% Change")
        work_sheet.update('E1', "Avg Vol 3mo")
        work_sheet.update('F1', "P/E Ratio")
        sleep(5.01)
        cellB = work_sheet.range('B2:B101')
        cellC = work_sheet.range('C2:C104')
        cellD = work_sheet.range('D2:D101')
        cellE = work_sheet.range('E2:E101')
        cellF = work_sheet.range('F2:F101')

        for i,row in enumerate(rows):
            cells = row.findChildren('td')
            for idx,cell in enumerate(cells):
                value = cell.string
                # Ticker 
                if idx == 0:
                    cellB[count].value = value
                # Price
                if idx == 2:
                    cellC[count].value = value
                # Percent change daily
                if idx == 4:
                    cellD[count].value = value
                    s = value.split('%')[0]
                    if "+" in s:
                        s1 = s.split('+')[1]
                        total += float(s1)
                    elif "-" in s:
                        s1 = s.split('-')[1]
                        total -= float(s1)
                # avg volume
                if idx == 6:
                    s = str(cell)
                    s1 = s.split('-->')[1]
                    s2 = s1.split('<!--')[0]
                    cellE[count].value = s2
                    s3 = s2.replace(",","")
                    if "M" in s3:
                        s4 = s3.split('M')[0]
                        avgVolume += float(s4)*1000000
                    else:
                        avgVolume += float(s3)
                # PE ratio
                if idx == 8:
                    if value != 'N/A':
                        s = str(cell)
                        s1 = s.split('-->')[1]
                        s2 = s1.split('<!--')[0]
                        cellF[count].value = s2
                        s3 = s2.replace(",","")
                        peTotal += float(s3)
                        # print(s3, end =" ")
                    else:
                        start_time = datetime.datetime.now()
                        cellF[count].value = value
                    count += 1
        #print()  
        
        change = "{:.2f}".format(total/i)+"%"
        peRatio = "{:.4f}".format(peTotal/i)
        avg3mo = "{:,.2f}".format(avgVolume/i)
        
        cellA = work_sheet.range('A102:A104')
        cellA[0].value = "Average % change"
        cellA[1].value = "Average PE Ratio"
        cellA[2].value = "Average Volume 3 mo"
        cellC[count].value = change
        count+=1
        cellC[count].value = peRatio
        count+=1
        cellC[count].value = avg3mo
        work_sheet.update_cells(cellA)
        work_sheet.update_cells(cellB)
        work_sheet.update_cells(cellC)    
        work_sheet.update_cells(cellD)
        work_sheet.update_cells(cellE)
        work_sheet.update_cells(cellF)
        sleep(6.01)
        print("Average % Change: "+ change)
        print("Average PE Ratio: "+peRatio)
        print("Average Volume (3 mo): "+avg3mo)
        print()
    else: 
        print("Error") 


def tech():
    url = 'https://finance.yahoo.com/sector/ms_technology' 
    sector = 'Technology'
    scrap(url, sector)

def financial():
    url='https://finance.yahoo.com/sector/ms_financial_services'
    sector = 'Financial'
    scrap(url, sector)

def basicMaterial():
    url='https://finance.yahoo.com/sector/ms_basic_materials'
    sector = 'Basic Material'
    scrap(url, sector)

def CommunicationService():
    url='https://finance.yahoo.com/sector/ms_communication_services'
    sector = 'Communication Service'
    scrap(url, sector)

def ConsumerCyclical():
    url='https://finance.yahoo.com/sector/ms_consumer_cyclical'
    sector = 'Consumer Cyclical'
    scrap(url, sector)

def ConsumerDefensive():
    url='https://finance.yahoo.com/sector/ms_consumer_defensive'
    sector = 'Consumer Defensive'
    scrap(url, sector)

def HealthCare():
    url='https://finance.yahoo.com/sector/ms_healthcare'
    sector = 'Health Care'
    scrap(url, sector)

def Industrial():
    url='https://finance.yahoo.com/sector/ms_industrials'
    sector = 'Industrial'
    scrap(url, sector)

def RealEstate():
    url='https://finance.yahoo.com/sector/ms_real_estate'
    sector = 'Real Estate'
    scrap(url, sector)

def Utilities():
    url='https://finance.yahoo.com/sector/ms_utilities'
    sector = 'Utilities'
    scrap(url, sector)

def Energy():
    url='https://finance.yahoo.com/sector/ms_energy'
    sector = 'Energy'
    scrap(url, sector)




tech()
financial()
basicMaterial()
CommunicationService()
ConsumerCyclical()
ConsumerDefensive()
HealthCare()
Industrial()
RealEstate()
Utilities()
Energy()