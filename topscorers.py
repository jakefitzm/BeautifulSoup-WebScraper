import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.espn.com/soccer/stats/_/league/fifa.worldq.uefa'

def get_top_scorers_table(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    scorerslist = []
    top_scorers_table = soup.find('div', class_='ResponsiveTable top-score-table' )
    for player in top_scorers_table.find_all('tbody', class_='Table__TBODY'):
        rows = player.find_all('tr')
        for row in rows[:10]:
            top_scorer = row.find_all('td', class_='Table__TD')[1].text
            scorer_team = row.find_all('td', class_='Table__TD')[2].text
            scorer_goals = row.find_all('td', class_='Table__TD')[4].text
            topscorers = {
                'Name' : top_scorer,
                'Team' : scorer_team,
                'Goals' : scorer_goals
            }
            scorerslist.append(topscorers)
    return scorerslist

data = get_top_scorers_table('https://www.espn.com/soccer/stats/_/league/fifa.worldq.uefa')

df = pd.DataFrame(data)
print('Here are the Top Scorers in the Qatar World Cup 2022 and qualifying stages:\n', df.head(10))
df.to_csv('scorers.csv')
print('saved in csv file')


a = pd.read_csv("scorers.csv")
a.to_html("scorersTable.html")
html_file = a.to_html()