import requests
from bs4 import BeautifulSoup
import pandas as pd

#URL to be scraped
url = 'https://www.espn.com/soccer/stats/_/league/fifa.worldq.uefa'

#Defining the function
def get_top_assists_table(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    assistslist = []
    # to select the right table
    top_assists_table = soup.find('div', class_='ResponsiveTable top-assists-table' )
    for player in top_assists_table.find_all('tbody', class_='Table__TBODY'):
        #To find the rows tr and only scrape the first ten rows
        rows = player.find_all('tr')
        for row in rows[:10]:
            #To find the required data in td
            top_assists = row.find_all('td', class_='Table__TD')[1].text
            assists_team = row.find_all('td', class_='Table__TD')[2].text
            player_assists = row.find_all('td', class_='Table__TD')[4].text
            topassists = {
                'Name' : top_assists,
                'Team' : assists_team,
                'Assists' : player_assists
            }
            assistslist.append(topassists)
    return assistslist

data = get_top_assists_table('https://www.espn.com/soccer/stats/_/league/fifa.worldq.uefa')

#output to dataframe
df = pd.DataFrame(data)
print('Here are the Players with the Most Assists in the Qatar World Cup 2022 and Qualifying Stages:\n', df.head(10))
df.to_csv('assists.csv')
print('saved in csv file')

#read the csv file
a = pd.read_csv("assists.csv")
 
# to save as html file named assistsTable.html
a.to_html("assistsTable.html")
html_file = a.to_html()