import requests
from bs4 import BeautifulSoup
url = 'https://sportsbrief.com/facts/teams/16181-argentina-national-football-teams-players-coach-fifa-world-rankings-world-cup-more/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Argentina National Team\n")
for tag in soup.find_all("li")[34:52]:
    print(tag.text)
    
    with open("argentina.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16412-saudi-arabia-national-football-team-players-coach-fifa-world-rankings-world-cup-2022-trophies/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout Saudi Arabia National Team\n")
for tag in soup.find_all("li")[34:48]:
    print(tag.text)
    
    with open("saudiarabia.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16393-mexicos-national-football-team-coach-fifa-world-rankings-world-cup-2022/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Mexico National Team\n")
for tag in soup.find_all("li")[34:50]:
    print(tag.text)
    
    with open("mexico.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16420-poland-national-football-team-players-coach-fifa-world-rankings-world-cup-2022/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Poland National Team\n")
for tag in soup.find_all("li")[34:49]:
    print(tag.text)
    
    with open("poland.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')