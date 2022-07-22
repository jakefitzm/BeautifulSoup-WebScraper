import requests
from bs4 import BeautifulSoup

url = 'https://sportsbrief.com/facts/teams/16210-portugal-national-football-team-players-coach-fifa-world-rankings-world-cup/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Portugal National Team\n")
for tag in soup.find_all("li")[34:50]:
    print(tag.text)
    
    with open("portugal.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/10791-ghana-national-football-team-players-coach-fifa-world-rankings-afcon/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Ghana National Team\n")
for tag in soup.find_all("li")[34:48]:
    print(tag.text)
    
    with open("ghana.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')
url = 'https://sportsbrief.com/facts/teams/16405-uruguays-national-football-team-players-coach-fifa-world-rankings-world-cup-2022-trophies/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Uruguay National Team\n")
for tag in soup.find_all("li")[34:43]:
    print(tag.text)
    
    with open("uruguay.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16289-south-korea-national-football-teams-players-coach-fifa-world-rankings-world-cup-2022-trophies-more/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The South Korea National Team\n")
for tag in soup.find_all("li")[34:52]:
    print(tag.text)
    
    with open("southkorea.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')