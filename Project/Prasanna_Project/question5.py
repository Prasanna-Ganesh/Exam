import csv
#i just tried to open the file by using csv but it doesn't open
csvFile = csv.reader(open('https://reqres.in/api/users?page=1'),"rb")
for i in csvFile:
    print(i)
# import pandas as pd
# import requests
# url='https://reqres.in/api/users'
# s=requests.get(url).content
# c=pd.read_csv(s)