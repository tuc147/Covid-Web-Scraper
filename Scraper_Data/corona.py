import bs4
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import numpy as np



page = requests.get('https://www.bbc.com/news/world-51235105') #Grabbing the page for scraping
parsed =  soup(page.content, 'html.parser') #Setting it to a readable format
table = parsed.find(id="newsspec-26926")
rows = table.find_all(class_="core__row")
countries = table.find_all(class_="c__r c__h--v")
cases = table.find_all(class_="c__c c__c--t")
deaths = table.find_all(class_="c__c c__c--d")

con = []
dth = []
cs = []
for i in range(len(countries)):
    con.append(countries[i].get_text().strip())
for i in range(len(cases)):
    cs.append(cases[i].get_text().strip())
for i in range(len(deaths)):
    dth.append(deaths[i].get_text().strip())

transfer = pd.DataFrame()
transfer.insert(0,column='Deaths',value=dth,allow_duplicates='true')
transfer.insert(0,column='Cases',value=cs,allow_duplicates='true')
transfer.insert(0,column='Country', value=con,allow_duplicates='true')

transfer.to_json(orient='records',path_or_buf="C:\\Users\\samft\\OneDrive\\CodeThings\\personal fuckery\\Covid Tracker\\Frontend\\covidValues2.json")

print(transfer.to_json(orient='records'))