import requests
from bs4 import BeautifulSoup

url = 'https://sportsbrief.com/facts/teams/16185-belgium-national-football-team-players-coach-fifa-world-rankings-world-cup/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Belgium National Team\n")
for tag in soup.find_all("li")[34:43]:
    print(tag.text)
    
    with open("belgium.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16398-canada-national-football-team-players-coach-fifa-world-rankings-world-cup-2022-trophies/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Canada National Team\n")
for tag in soup.find_all("li")[34:47]:
    print(tag.text)
    
    with open("canada.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/10713-morocco-national-football-team-squad-coach-world-rankings-afcon-nickname/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Morocco National Team\n")
for tag in soup.find_all("li")[34:46]:
    print(tag.text)
    
    with open("morocco.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16225-croatia-national-football-teams-players-coach-fifa-world-rankings-world-cup-2022-more/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Croatia National Team\n")
for tag in soup.find_all("li")[34:52]:
    print(tag.text)
    
    with open("croatia.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')