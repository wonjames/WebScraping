import requests 
from bs4 import BeautifulSoup 
  
def tech(): 
    # the target we want to open     
    url='https://finance.yahoo.com/screener/predefined/technology/'
      
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        
        print("Tech Sector Yahoo Finance :") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     

        l=soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')
        total = 0
        for i,row in enumerate(rows):
                cells = row.findChildren('td')
                for idx,cell in enumerate(cells):
                    value = cell.string
                    #if idx == 0 or idx == 4:
                    #    print(value, end =" ")
                    if idx == 4:
                        s = value.split('%')[0]
                        if "+" in s:
                            s1 = s.split('+')[1]
                            total += float(s1)
                        else:
                            s1 = s.split('-')[1]
                            total -= float(s1)
                        
                        
                #print()      
        print("Total % Change:", total/i)
        print()
    else: 
        print("Error") 

def financial():
    
    url='https://finance.yahoo.com/sector/ms_financial_services'
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        
        print("Financial Sector Yahoo Finance :") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     

        l=soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')
        total = 0
        for i,row in enumerate(rows):
                cells = row.findChildren('td')
                for idx,cell in enumerate(cells):
                    value = cell.string
                    #if idx == 0 or idx == 4:
                    #   print(value, end =" ")
                    if idx == 4:
                        s = value.split('%')[0]
                        if "+" in s:
                            s1 = s.split('+')[1]
                            total += float(s1)
                        elif "-" in s:
                            s1 = s.split('-')[1]
                            total -= float(s1)
                        
                        
                #print()      
        print("Total % Change:", total/i)
        print()
    else: 
        print("Error") 

def basicMaterial():
    
    url='https://finance.yahoo.com/sector/ms_basic_materials'
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        
        print("Basic Materials Sector Yahoo Finance :") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     

        l=soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')
        total = 0
        for i,row in enumerate(rows):
                cells = row.findChildren('td')
                for idx,cell in enumerate(cells):
                    value = cell.string
                    #if idx == 0 or idx == 4:
                        #print(value, end =" ")
                    if idx == 4:
                        s = value.split('%')[0]
                        if "+" in s:
                            s1 = s.split('+')[1]
                            total += float(s1)
                        elif "-" in s:
                            s1 = s.split('-')[1]
                            total -= float(s1)
                        
                        
                #print()      
        print("Total % Change:", total/i)
        print()
    else: 
        print("Error") 

def CommunicationService():
    
    url='https://finance.yahoo.com/sector/ms_communication_services'
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        
        print("Communication Sector Yahoo Finance :") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     

        l=soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')
        total = 0
        for i,row in enumerate(rows):
                cells = row.findChildren('td')
                for idx,cell in enumerate(cells):
                    value = cell.string
                    #if idx == 0 or idx == 4:
                        #print(value, end =" ")
                    if idx == 4:
                        s = value.split('%')[0]
                        if "+" in s:
                            s1 = s.split('+')[1]
                            total += float(s1)
                        elif "-" in s:
                            s1 = s.split('-')[1]
                            total -= float(s1)
                        
                        
                #print()      
        print("Total % Change:", total/i)
        print()
    else: 
        print("Error") 

def ConsumerCyclical():
    
    url='https://finance.yahoo.com/sector/ms_consumer_cyclical'
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        
        print("Consumer Cyclical Sector Yahoo Finance :") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     

        l=soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')
        total = 0
        for i,row in enumerate(rows):
                cells = row.findChildren('td')
                for idx,cell in enumerate(cells):
                    value = cell.string
                    #if idx == 0 or idx == 4:
                        #print(value, end =" ")
                    if idx == 4:
                        s = value.split('%')[0]
                        if "+" in s:
                            s1 = s.split('+')[1]
                            total += float(s1)
                        elif "-" in s:
                            s1 = s.split('-')[1]
                            total -= float(s1)
                        
                        
                #print()      
        print("Total % Change:", total/i)
        print()
    else: 
        print("Error") 

def ConsumerDefensive():
    
    url='https://finance.yahoo.com/sector/ms_consumer_defensive'
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        
        print("Consumer Defensive Sector Yahoo Finance :") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     

        l=soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')
        total = 0
        for i,row in enumerate(rows):
                cells = row.findChildren('td')
                for idx,cell in enumerate(cells):
                    value = cell.string
                    #if idx == 0 or idx == 4:
                        #print(value, end =" ")
                    if idx == 4:
                        s = value.split('%')[0]
                        if "+" in s:
                            s1 = s.split('+')[1]
                            total += float(s1)
                        elif "-" in s:
                            s1 = s.split('-')[1]
                            total -= float(s1)
                        
                        
                #print()      
        print("Total % Change:", total/i)
        print()
    else: 
        print("Error") 

def HealthCare():
    
    url='https://finance.yahoo.com/sector/ms_healthcare'
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        
        print("Healthcare Sector Yahoo Finance :") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     

        l=soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')
        total = 0
        for i,row in enumerate(rows):
                cells = row.findChildren('td')
                for idx,cell in enumerate(cells):
                    value = cell.string
                    #if idx == 0 or idx == 4:
                        #print(value, end =" ")
                    if idx == 4:
                        s = value.split('%')[0]
                        if "+" in s:
                            s1 = s.split('+')[1]
                            total += float(s1)
                        elif "-" in s:
                            s1 = s.split('-')[1]
                            total -= float(s1)
                        
                        
                #print()      
        print("Total % Change:", total/i)
        print()
    else: 
        print("Error") 

def Industrial():
    
    url='https://finance.yahoo.com/sector/ms_industrials'
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        
        print("Industrial Sector Yahoo Finance :") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     

        l=soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')
        total = 0
        for i,row in enumerate(rows):
                cells = row.findChildren('td')
                for idx,cell in enumerate(cells):
                    value = cell.string
                    #if idx == 0 or idx == 4:
                        #print(value, end =" ")
                    if idx == 4:
                        s = value.split('%')[0]
                        if "+" in s:
                            s1 = s.split('+')[1]
                            total += float(s1)
                        elif "-" in s:
                            s1 = s.split('-')[1]
                            total -= float(s1)
                        
                        
                #print()      
        print("Total % Change:", total/i)
        print()
    else: 
        print("Error") 

def RealEstate():
    
    url='https://finance.yahoo.com/sector/ms_real_estate'
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        
        print("Real Estate Sector Yahoo Finance :") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     

        l=soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')
        total = 0
        for i,row in enumerate(rows):
                cells = row.findChildren('td')
                for idx,cell in enumerate(cells):
                    value = cell.string
                    #if idx == 0 or idx == 4:
                        #print(value, end =" ")
                    if idx == 4:
                        s = value.split('%')[0]
                        if "+" in s:
                            s1 = s.split('+')[1]
                            total += float(s1)
                        elif "-" in s:
                            s1 = s.split('-')[1]
                            total -= float(s1)
                        
                        
                #print()      
        print("Total % Change:", total/i)
        print()
    else: 
        print("Error") 
def Utilities():
    
    url='https://finance.yahoo.com/sector/ms_utilities'
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        
        print("Utilities Sector Yahoo Finance :") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     

        l=soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')
        total = 0
        for i,row in enumerate(rows):
                cells = row.findChildren('td')
                for idx,cell in enumerate(cells):
                    value = cell.string
                    #if idx == 0 or idx == 4:
                        #print(value, end =" ")
                    if idx == 4:
                        s = value.split('%')[0]
                        if "+" in s:
                            s1 = s.split('+')[1]
                            total += float(s1)
                        elif "-" in s:
                            s1 = s.split('-')[1]
                            total -= float(s1)
                        
                        
                #print()      
        print("Total % Change:", total/i)
        print()
    else: 
        print("Error") 
def Energy():
    
    url='https://finance.yahoo.com/sector/ms_energy'
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        
        print("Energy Sector Yahoo Finance :") 
      
        # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')     

        l=soup.find("table",{"class":"W(100%)"}) 
        rows = l.findChildren('tr')
        total = 0
        for i,row in enumerate(rows):
                cells = row.findChildren('td')
                for idx,cell in enumerate(cells):
                    value = cell.string
                    #if idx == 0 or idx == 4:
                        #print(value, end =" ")
                    if idx == 4:
                        s = value.split('%')[0]
                        if "+" in s:
                            s1 = s.split('+')[1]
                            total += float(s1)
                        elif "-" in s:
                            s1 = s.split('-')[1]
                            total -= float(s1)
                        
                        
                #print()      
        print("Total % Change:", total/i)
        print()
    else: 
        print("Error") 
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