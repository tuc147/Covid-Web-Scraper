import bs4
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import numpy as np



page = requests.get('https://www.nytimes.com/interactive/2020/world/coronavirus-maps.html#countries') #Grabbing the page for scraping
scrape = soup(page.content, 'html.parser') #Setting it to a readable format
table = scrape.find(id='countries') #<div> Containing the information 
 
countries = table.find_all(class_="text svelte-yabvh9") #All the countries in the table
casesToDeaths = table.find_all(class_="num svelte-yabvh9 toggleable") #All cases and deaths in alternating order / every other entry is another country
subS = (str(countries[0].get_text())) #get_text() retireves text contained within the tag 

con = []
for i in range(len(countries)):
    con.append((countries[i].get_text()).strip()) #Entering countries as strings into the list: con to write to a csv file / Use split to remove extra whitespace
cases = []
deaths = []   
for i in range(len(casesToDeaths)):
    if i%2==0:
        cases.append((casesToDeaths[i].get_text()).strip()) #Entering cases(First value of two) as strings into the list: cases to write to a csv file
    else:
        deaths.append((casesToDeaths[i].get_text()).strip()) #Entering deaths(Second value of two) as strings into the list: deaths to write to a csv file

covidTable = pd.DataFrame(index=con,columns=['Cases','Deaths'])


print(covidTable.columns(str(con[2]))
#print(covidTable.to_numpy)

