import requests
from bs4 import BeautifulSoup
url = 'https://sportsbrief.com/facts/teams/16190-france-national-football-teams-players-coach-fifa-world-rankings-world-cup-more/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The France National Team\n")
for tag in soup.find_all("li")[34:52]:
    print(tag.text)
    
    with open("france.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')


url = 'https://sportsbrief.com/facts/teams/16235-denmark-national-football-teams-players-coach-fifa-world-rankings-world-cup-2022-trophies-more/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Denmark National Team\n")
for tag in soup.find_all("li")[34:52]:
    print(tag.text)
    
    with open("denmark.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/10582-tunisia-national-football-team-squad-coach-world-rankings-afcon-nickname/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Tunisia National Team\n")
for tag in soup.find_all("li")[34:44]:
    print(tag.text)
    
    with open("tunisia.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')