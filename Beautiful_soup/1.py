import bs4 as bs
import urllib.request
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import matplotlib
import csv
import numpy as np
import pandas as pd

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/2017%E2%80%9318_Indian_Super_League_season').read()

soup = bs.BeautifulSoup(source,'lxml')

table_classes = {"class": ["wikitable", "plainrowheaders"]}
wikitables = soup.findAll("table", table_classes)

f=wikitables[4]

t = PrettyTable(['Team', 'Pld', 'W', 'D','L', 'GF', 'GA', 'GD' , 'Pts', 'Qualification or relegation'])

table_rows = f.find_all('tr')

rows_list = []

df=pd.DataFrame(columns=['Team', 'Pld', 'W', 'D','L', 'GF', 'GA', 'GD' , 'Pts', 'Qualification or relegation'])

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    k = len(row)
    if(k==9):
        row.append(" ")
    #print(row)
    if(len(row) == 10):
        t.add_row(row)
        rows_list.append(row)

for row in rows_list:
    df.loc[len(df)] = row

print (t)

print()

#Lables=["
plt.barh(df['Team'],df['Pts'])
plt.show()
#df.plot(x=" ", y=['Pld', 'W', 'D','L', 'GF', 'GA', 'GD' , 'Pts'], kind="bar")



#soup.find_all('table', class_='wikitable sortable plainrowheaders')

#print (soup.prettify)
'''
teams = []
rows = soup.findAll('tr', {'class': ''})
for row in range(len(rows)):
    team_row = []
    columns = rows[row].findAll('td')
    for column in columns:
        team_row.append(column.getText())
    #print(team_row)
    # Add each team to a teams matrix.
    teams.append(team_row)
'''
