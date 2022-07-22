import requests
from bs4 import BeautifulSoup

url = 'https://sportsbrief.com/facts/teams/16226-brazil-national-football-team-players-coach-fifa-world-rankings-world-cup/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Brazil National Team\n")
for tag in soup.find_all("li")[34:46]:
    print(tag.text)
    
    with open("brazil.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16343-serbia-national-football-team-players-coach-fifa-world-rankings-world-cup-2022-trophies/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Serbia National Team\n")
for tag in soup.find_all("li")[34:45]:
    print(tag.text)
    
    with open("serbia.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16372-switzerlands-national-football-teams-players-coach-fifa-world-rankings-world-cup2022-trophies/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Switzerland National Team\n")
for tag in soup.find_all("li")[34:50]:
    print(tag.text)
    
    with open("switzerland.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/10704-cameroon-national-football-team-squad-coach-world-rankings-afcon-trophies/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Cameroon National Team\n")
for tag in soup.find_all("li")[34:47]:
    print(tag.text)
    
    with open("cameroon.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')