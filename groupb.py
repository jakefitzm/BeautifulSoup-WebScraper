import requests
from bs4 import BeautifulSoup
url = 'https://sportsbrief.com/facts/teams/16254-england-national-football-team-players-coach-fifa-world-rankings-world-cup/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The England National Team\n")
for tag in soup.find_all("li")[34:49]:
    print(tag.text)
    
    with open("england.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16355-irans-national-football-team-players-coach-fifa-world-rankings-world-cup-2022-trophies/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout Iran National Team\n")
for tag in soup.find_all("li")[34:43]:
    print(tag.text)
    
    with open("iran.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16396-usa-national-football-teams-players-coach-fifa-world-rankings-world-cup-2022/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The USA National Team\n")
for tag in soup.find_all("li")[34:49]:
    print(tag.text)
    
    with open("usa.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')
