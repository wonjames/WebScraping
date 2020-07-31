import requests 
from bs4 import BeautifulSoup 
  
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

def key_s(arr):
    s1 = "https://finance.yahoo.com/quote/"
    s2 = "/key-statistics?p="

    for ticker in arr:
        s3 = s1 + ticker + s2 + ticker
        resp = requests.get(s3)
        
        if resp.status_code==200: 
      
            # we need a parser,Python built-in HTML parser is enough . 
            soup = BeautifulSoup(resp.text,'html.parser')     
            num = 0
            while num < 3:
                l = soup.find_all("table",{"class":"W(100%) Bdcl(c)"})[num]

                rows = l.findChildren('tr')

                for i,row in enumerate(rows):
                        cells = row.findChildren('td')
                        for idx,cell in enumerate(cells):
                            if idx == 0:
                                name = cell
                                if name.text.endswith("1") or name.text.endswith("2") or name.text.endswith("3") or name.text.endswith("4") or name.text.endswith("5"):
                                    str = name.text[:-1]
                                    print(str, end=" ")
                                else:
                                    print(name.text, end=" ")
                            else:
                                value = cell.string
                                print(value)
                num += 1
                        
        else: 
            print("Error")

def tech():
    url = 'https://finance.yahoo.com/sector/ms_technology' 
    sector = 'Technology'
    arr = scrap(url, sector)
    narr = ["AAPL"]
    key_s(narr)
tech()