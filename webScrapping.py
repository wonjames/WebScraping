import requests 
from bs4 import BeautifulSoup 
  
def scrap(newUrl, sector):
    url=newUrl
      
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        
        print(sector, "Sector:") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     

        l=soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')
        total = 0
        peTotal = 0
        for i,row in enumerate(rows):
                cells = row.findChildren('td')
                for idx,cell in enumerate(cells):
                    value = cell.string
                    if idx == 0 or idx == 4:
                        print(value, end =" ")
                    if idx == 4:
                        s = value.split('%')[0]
                        if "+" in s:
                            s1 = s.split('+')[1]
                            total += float(s1)
                        elif "-" in s:
                            s1 = s.split('-')[1]
                            total -= float(s1)
                    
                    if idx == 8:
                        if value != 'N/A':
                            s = str(cell)
                            s1 = s.split('-->')[1]
                            s2 = s1.split('<!--')[0]
                            s3 = s2.replace(",","")
                            peTotal += float(s3)
                            print(s3, end =" ")
                        else:
                            print("N/A", end = " ")
                        
                print()      
        print("Total % Change: "+"{:.4f}".format(total/i))
        print("Total PE Ratio: "+"{:.4f}".format(peTotal/i))
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
    sector = 'Consumer Syclical'
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