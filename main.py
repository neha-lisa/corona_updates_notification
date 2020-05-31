# This Code was written on 5-May-2020 by Neha 
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,Message):
    notification.notify(
        title = title,
        message = Message,
        app_icon =  "icon.ico",
        timeout = 15
    )

def getData(url):
    r = requests.get(url)
    return r.text

while True:
    if __name__ =="__main__":
        # notifyMe("Neha","Lets stop this virus together")
        myHtmlData = getData("https://www.mohfw.gov.in/")

        # print(myHtmlData)
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        myDataStr = ""
        for table in soup.find_all('tbody'):
            # print(table.get_text())
            myDataStr += (table.get_text())
        myDataStr = myDataStr[1:]
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n\n")
        states = ['6','31','32']
    
        for i in itemList[0:34]:
            dataList = i.split('\n')
            # print(dataList)
            if dataList[0] in states:
                print(dataList)
                ntitle= 'Cases of Covid-19'
                ntext = f"{dataList[1]} :- \n Confirmed Cases : {dataList[2]}\n Cured: {dataList[3]}\n Deaths: {dataList[4]}"
                notifyMe(ntitle,ntext)
                time.sleep(2)
        time.sleep(2)   



    
 
    # states = ['Chandigarh','West Bengal','Uttar Pradesh']
    # for item in itemList[1:34]:
    #     dataList = item.split("\n")
    #     print(dataList)

    