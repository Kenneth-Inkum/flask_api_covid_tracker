import requests

import csv

from io import StringIO

from app import URL

res=requests.get(URL)


data =res.content.decode('ascii', 'ignore')


csv_data=StringIO(data)

reader= csv.reader(csv_data)

for row in reader:
    print(row)