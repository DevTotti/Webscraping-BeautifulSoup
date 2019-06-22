import requests 
from bs4 import BeautifulSoup as bsp

request = requests.get("https://grabthebeast.com/watch.php?tvshow=34524&season=2&episode=1")

print (request.status_code)

src = request.content

soup = bsp(src,'lxml')

links = soup.find_all("a")
print(links)

print ("\n")

#for link in links