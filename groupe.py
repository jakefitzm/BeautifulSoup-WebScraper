import requests
from bs4 import BeautifulSoup

url = 'https://sportsbrief.com/facts/teams/16271-spains-national-football-teams-players-coach-fifa-world-rankings-world-cup/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Spain National Team\n")
for tag in soup.find_all("li")[34:49]:
    print(tag.text)
    
    with open("spain.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16322-germany-national-football-team-players-coach-fifa-world-rankings-world-cup/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Germany National Team\n")
for tag in soup.find_all("li")[34:43]:
    print(tag.text)
    
    with open("germany.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16309-japan-national-football-teams-players-coach-fifa-world-rankings-world-cup-2022-trophies-more/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Japan National Team\n")
for tag in soup.find_all("li")[34:43]:
    print(tag.text)
    
    with open("japan.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')