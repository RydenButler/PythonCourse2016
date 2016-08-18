from bs4 import BeautifulSoup
from django.utils.encoding import smart_str, smart_unicode
from urlparse import *
import urllib2 
import random
import time
import os
import re
import csv

address = 'https://petitions.whitehouse.gov/petitions'

#Save_Petitions(address)

def Save_Petitions(website):
	with open('HW2_Output.csv', 'wb') as f:
		writer = csv.DictWriter(f, fieldnames = ("PetitionTitle", "UploadDate", "IssueTags", "Signatures"))
		writer.writeheader()

		Titles, Dates, Tags, Sigs = Scrape_Petitions(website)

		for i in range(len(Titles)):
			writer.writerow({'PetitionTitle':Titles[i], 'UploadDate': Dates[i], 'IssueTags': Tags[i], 'Signatures': Sigs[i]})

def Scrape_Petitions(website):
	Headers, Tags, Sigs = get_Headers_Tags_Sigs(website)
	Links, Titles = get_Links_Titles(Headers)
	Dates = get_Dates(Links)
	return Titles, Dates, Tags, Sigs

def get_Headers_Tags_Sigs(website):
	Headers = []
	Tag_Lists = []
	Tags = []
	Signatures = []
	for i in range(4):
		web_page = urljoin(str(website), '?page=%d' % i)
		web_text = urllib2.urlopen(web_page)
		soup = BeautifulSoup(web_text.read())
		Headers.extend(soup.find_all('h3'))
		sigs = soup.find_all('span', {'class': 'signatures-number'})
		for sig in sigs:
			Signatures.append(str(sig.get_text()))
		tag_list = soup.find_all('div', {'class': "field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags"})
		for item in tag_list:
			Tag_Lists.append(item.find_all('h6'))
		for List in Tag_Lists:
			tags = []
			for tag in List:
				tags.append(str(tag.get_text()))
			Tags.append(tags)
	Tags = Tags[-74:]
	return Headers, Tags, Signatures

def get_Links_Titles(petitions):
	Links = []
	Titles = []
	for petition in petitions:
		try:
			extension = petition.a['href']
		except:
			continue
		else:
			Titles.append(smart_str(petition.a.get_text()))
			Links.append(urljoin("https://petitions.whitehouse.gov", str(extension)))
	return Links, Titles

def get_Dates(Links):
	Dates = []
	for link in Links:
		web_text = urllib2.urlopen(link)
		soup = BeautifulSoup(web_text.read())
		attrib = soup.find_all('h4', {'class': 'petition-attribution'})
		text_att = str(attrib[0].get_text())
		words = text_att.split()
		Dates.append(' '.join(words[-3:]))
	return Dates