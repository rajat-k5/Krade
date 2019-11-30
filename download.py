import requests
import zipfile
import os
import time
from datetime import datetime

now = datetime.now()
months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
print('Beginning file download with requests')

weekend_check = now.strftime("%A")

holiday_check = now.strftime("%d-%b-%Y")
holidays_list = ["04-Mar-2019","21-Mar-2019","17-Apr-2019","19-Apr-2019","29-Apr-2019","01-May-2019","05-Jun-2019","12-Aug-2019","15-Aug-2019","02-Sep-2019",	
"10-Sep-2019","02-Oct-2019","08-Oct-2019","21-Oct-2019","28-Oct-2019","12-Nov-2019","25-Dec-2019"]

if holiday_check in holidays_list:
    exit(11)

if weekend_check == "Saturday" or weekend_check == "Sunday":
    exit(12)

url = 'https://www.nseindia.com/content/historical/EQUITIES/'+str(now.year)+'/'+months[now.month-1]+'/cm'+str(now.day)+months[now.month-1]+str(now.year)+'bhav.csv'


r = requests.get(url)


with open('data.zip', 'wb') as f:
    f.write(r.content)
with zipfile.ZipFile("data.zip", 'r') as zipObj:
    listOfFileNames = zipObj.namelist()
    for fileName in listOfFileNames:
        if fileName.endswith('.csv'):
            zipObj.extract(fileName)
            os.rename(fileName,"data"+str(time.time())+".csv")

os.remove("data.zip")