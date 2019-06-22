"""import requests
from bs4 import BeautifulSoup as bsp

request = requests.get("https://www.google.com")
#print (request.status_code)

#print (request.headers)

src  = request.content
#print (src)

soup = bsp(src, 'lxml')

links = soup.find_all("a")
#print (links)
#print ("\n")

for link in links:
	if "About" in link.text:
		print (link)
		print (link.attrs['href'])"""



"""
import requests
from bs4 import BeautifulSoup as bsp

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content

soup = bsp(src, 'lxml')

urls =[]

for h2_tags in soup.find_all("h2"):
	#print (h2_tags)
	a_tag = h2_tags.find('a')
	urls.append(a_tag.attrs['href'])

print (urls)
"""
