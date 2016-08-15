from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os
import re

web_address = 'https://polisci.wustl.edu/faculty/specialization'

def find_profs(address):
	web_page = urllib2.urlopen(web_address)
	soup = BeautifulSoup(web_page.read())
	Specs = soup.find_all('h3')
	Names = []
	Titles = []
	Emails = []
	Pages = []
	Info = soup.find_all('div', {'class': 'views-row'})
	for i in range(len(Info)):
		Names.append(str(Info[i].get_text().split('\n')[1]))
		Titles.append(str(Info[i].get_text().split('\n')[2]))
	Subfields = []
	for sub in Specs:
		for sibling in sub.next_siblings:
			if sibling in Specs:
				break
			else:
				try:
					sibling.get_text()
					Subfields.append(sub)
				except:
					pass
	Extensions = soup.find_all('a',{'class':"person-view-primary-field" })
	appendage = []
	for x in Extensions:
		appendage.append(str(x['href']))
	Links = []
	for app in appendage:
		Links.append('http://polisci.wustl.edu%s' % app)
	for link in Links:
		new_page = urllib2.urlopen(link)
		new_soup = BeautifulSoup(new_page)
		Mid = new_soup.find_all('div', {'class': 'field-item even'})
		Mid2 = []
		Mid3 = []
		page = 'NA'
		for m in range(len(Mid)):
			Mid2.append(Mid[m].get_text())
		for i in range(len(Mid2)):
			if '@' in Mid2[i]:
				Emails.append(str(Mid2[i]))
			try:
				A = (str(Mid[i].contents[0]['href']))
			except:
				continue
			else:
				Mid3.append(str(Mid[i].contents[0]['href']))
		for j in range(len(Mid3)):
			if 'http://' in Mid3[j]:
				page = str(Mid3[j])
			else:
				continue
		Pages.append(page)
	return len(Names)

	with open('lab4.csv', 'wb') as f:
  		my_writer = csv.DictWriter(f, fieldnames=("Name", "Title", "Field", "Email", "Website"))
  		my_writer.writeheader()
  		for i in range(len(Names)):
    		my_writer.writerow({"Name":Names[i], "Title":Titles[i], "Field": Subfields[i], "Email": Emails[i], "Website": Pages[i]})


find_profs(web_address)


