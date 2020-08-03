import requests 
from bs4 import BeautifulSoup 
import gspread
import datetime
import time
from time import sleep

gc = gspread.oauth()
worksheet = None

# Get array of tickers from yahoo for each sector
def scrap(newUrl, sector):
    url = newUrl
    #open with GET method 
    resp = requests.get(url) 
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        # we need a parser,Python built-in HTML parser is enough . 
        soup = BeautifulSoup(resp.text,'html.parser')     
        l = soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')

        tickArr = [0] * 100
        for i,row in enumerate(rows):
                cells = row.findChildren('td')
                for idx,cell in enumerate(cells):
                    value = cell.string
                    if idx == 0:
                        tickArr[i-1] = value
    else: 
        print("Error") 

    return tickArr

# Gets the key statistics of each ticker individually
def key_s(arr, sh):
    s1 = "https://finance.yahoo.com/quote/"
    s2 = "/key-statistics?p="

    for ticker in arr:
        s3 = s1 + ticker + s2 + ticker
        resp = requests.get(s3)
        list_worksheets = sh.worksheets()
        check = False
        for wks in list_worksheets:
            if wks.title == ticker:
                check = True
                worksheet = sh.worksheet(ticker)
                break
        
        if check == False:
            worksheet = sh.add_worksheet(title=ticker, rows=110, cols=10)

        if resp.status_code==200: 
            # we need a parser,Python built-in HTML parser is enough . 
            soup = BeautifulSoup(resp.text,'html.parser')     
            num = 0
            count = 0
            worksheet.format('A1:B1', {    
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
            worksheet.update('A1', ticker)
            worksheet.update('B1', date)
            sleep(3.01)
            cellA = worksheet.range('A2:A51')
            cellC = worksheet.range('C2:C51')

            # gets the right table
            while num < 3:
                l = soup.find_all("table",{"class":"W(100%) Bdcl(c)"})[num]
                rows = l.findChildren('tr')

                for i,row in enumerate(rows):
                    cells = row.findChildren('td')
                    for idx,cell in enumerate(cells):
                        if idx == 0:
                            name = cell
                            if name.text.endswith("1") or name.text.endswith("2") or name.text.endswith("3") or name.text.endswith("4") or name.text.endswith("5"):
                                s = name.text[:-1]
                                cellA[count].value = s
                            else:
                                cellA[count].value = name.text
                        else:
                            value = cell.string
                            cellC[count].value = value
                            count += 1
                        
                num += 1
            # gets the left table 
            while num < 9:
                l = soup.find_all("table",{"class":"W(100%) Bdcl(c)"})[num]
                rows = l.findChildren('tr')

                for i,row in enumerate(rows):
                    cells = row.findChildren('td')
                    for idx,cell in enumerate(cells):
                        if idx == 0:
                            name = cell
                            if name.text.endswith("1") or name.text.endswith("2") or name.text.endswith("3") or name.text.endswith("4") or name.text.endswith("5"):
                                s = name.text[:-1]
                                cellA[count].value = s
                            else:
                                cellA[count].value = name.text
                        else:
                            value = cell.string
                            cellC[count].value = value
                            count += 1
                           
                num += 1

            worksheet.update_cells(cellA)
            worksheet.update_cells(cellC)
            sleep(3.01)
            print(ticker)
        else: 
            print("Error")

def tech():
    url = 'https://finance.yahoo.com/sector/ms_technology' 
    sector = 'Technology'
    arr = scrap(url, sector)
    title = "tech_key_stats"
    spreadsheetCheck(title)
    sh = gc.open(title)
    key_s(arr, sh)

def fin():
    url = 'https://finance.yahoo.com/sector/ms_financial_services' 
    sector = 'Financial'
    arr = scrap(url, sector)
    title = "fin_key_stats"
    spreadsheetCheck(title)
    sh = gc.open(title)
    key_s(arr, sh)

def basicMaterial():
    url='https://finance.yahoo.com/sector/ms_basic_materials'
    sector = 'Basic Material'
    arr = scrap(url, sector)
    title = "basic_material_key_stats"
    spreadsheetCheck(title)
    sh = gc.open(title)
    key_s(arr, sh)

def CommunicationService():
    url='https://finance.yahoo.com/sector/ms_communication_services'
    sector = 'Communication Service'
    arr = scrap(url, sector)
    title = "com_service_stats"
    spreadsheetCheck(title)
    sh = gc.open(title)
    key_s(arr, sh)

def ConsumerCyclical():
    url='https://finance.yahoo.com/sector/ms_consumer_cyclical'
    sector = 'Consumer Cyclical'
    arr = scrap(url, sector)
    title = "consumer_cyclical_key_stats"
    spreadsheetCheck(title)
    sh = gc.open(title)
    key_s(arr, sh)

def ConsumerDefensive():
    url='https://finance.yahoo.com/sector/ms_consumer_defensive'
    sector = 'Consumer Defensive'
    arr = scrap(url, sector)
    title = "consumer_defensive_key_stats"
    spreadsheetCheck(title)
    sh = gc.open(title)
    key_s(arr, sh)

def HealthCare():
    url='https://finance.yahoo.com/sector/ms_healthcare'
    sector = 'Health Care'
    arr = scrap(url, sector)
    title = "health_care_key_stats"
    spreadsheetCheck(title)
    sh = gc.open(title)
    key_s(arr, sh)

def Industrial():
    url='https://finance.yahoo.com/sector/ms_industrials'
    sector = 'Industrial'
    arr = scrap(url, sector)
    title = "industrial_key_stats"
    spreadsheetCheck(title)
    sh = gc.open(title)
    key_s(arr, sh)

def RealEstate():
    url='https://finance.yahoo.com/sector/ms_real_estate'
    sector = 'Real Estate'
    arr = scrap(url, sector)
    title = "real_estate_key_stats"
    spreadsheetCheck(title)
    sh = gc.open(title)
    key_s(arr, sh)

def Utilities():
    url='https://finance.yahoo.com/sector/ms_utilities'
    sector = 'Utilities'
    arr = scrap(url, sector)
    title = "utilities_key_stats"
    spreadsheetCheck(title)
    sh = gc.open(title)
    key_s(arr, sh)

def Energy():
    url='https://finance.yahoo.com/sector/ms_energy'
    sector = 'Energy'
    arr = scrap(url, sector)
    title = "energy_key_stats"
    spreadsheetCheck(title)
    sh = gc.open(title)
    key_s(arr, sh)

def spreadsheetCheck(title):
    title_list = []
    for spreadsheet in gc.openall():
        title_list.append(spreadsheet.title)
    if title not in title_list:
        gc.create(title)

tech()
fin()
basicMaterial()
CommunicationService()
ConsumerCyclical()
ConsumerDefensive()
HealthCare()
Industrial()
RealEstate()
Utilities()
Energy()