import newspaper 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from newspaper import Article
import validators

for i in range (0,100):
	s=str(i)
	req = Request("https://www.ledauphine.com/sante/coronavirus+region/alpes+region/paca+region/vallee-du-rhone+zone/france-monde?page="+s)
	html_page = urlopen(req)

	soup = BeautifulSoup(html_page, "lxml")

	links = []
	for link in soup.findAll('a'):
		lien=link.get('href')		
		if (lien is not None)  and    (not "void" in lien)    and     (lien  not in link)     :
				links.append(lien)	
							
for i in range (0,len(links)):
	if not "ledauphine" in links[i]:	
		links[i]="https://www.ledauphine.com"+links[i]	
	print(links[i])
		
for url in links: 
	try:
			article = Article(url)
			article.download()
			article.parse()
			texte=article.text
			if not "Siret" in texte:
				print(texte)
	except: print("erreur")
