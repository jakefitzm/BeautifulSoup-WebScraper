import requests
from bs4 import BeautifulSoup

#requesting the Web page to be scraped 
url = 'https://sportsbrief.com/facts/teams/16305-qatar-national-football-team-players-coach-fifa-world-rankings-world-cup/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

#displaying text in the Python terminal
print("\nAbout The Qatar National Team\n")
#Scraping specific lines from a list stored in <li> tags in <ul> tags and printing
for tag in soup.find_all("li")[34:47]:
    print(tag.text)
    
    #opening a html file in append mode and appending the scraped data to a new line
    #'\n' does not affect the HTML output but makes the html file easier to read in code editor as each item is on a new list
    with open("qatar.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16367-ecuador-national-football-team-players-coach-fifa-world-rankings-world-cup-2022-trophies/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

#to scrape between the 34th and 46th line in the <li> tags
print("\nAbout The Ecuador National Team\n")
for tag in soup.find_all("li")[34:46]:
    print(tag.text)
    
    with open("ecuador.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/10696-senegal-national-football-team-squad-coach-world-rankings-afcon-nickname/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Senegal National Team\n")
for tag in soup.find_all("li")[34:47]:
    print(tag.text)
    
    with open("senegal.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')

url = 'https://sportsbrief.com/facts/teams/16212-netherlands-national-football-team-players-coach-fifa-world-rankings-world-cup/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("\nAbout The Netherlands National Team\n")
for tag in soup.find_all("li")[34:50]:
    print(tag.text)
    
    with open("netherlands.html", "a", encoding='utf-8') as file:
        file.write(tag.text+'<br>'+'\n')