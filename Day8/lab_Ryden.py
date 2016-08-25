import re

# open text file of 2008 NH primary Obama speech
file = open("obama-nh.txt", "r")
text = file.readlines()
file.close()

# compile the regular expression
keyword = re.compile(r"the ")

# search file for keyword, line by line
for line in text:
  if not keyword.search(line):
    print line 

# TODO: print all lines that DO NOT contain "the "
for line in text:
  if not keyword.search(line):
    print line 

# TODO: print lines that contain a word of any length starting with s and ending with e
# re.compile(r"\As+\w*e\z")
keyword = re.compile(r"\bs\w*e\b")
for line in text:
	if keyword.search(line):
		print line
  
date = raw_input("Please enter a date in the format MM.DD.YY: ")
print '''
Month: %s
Day: %s
Year: %s
 ''' % (re.findall(r"(\d+)", date)[0], re.findall(r"(\d+)", date)[1], re.findall(r"(\d+)", date)[2])
# Print the date input in the following format:
# Month: MM
# Day: DD
# Year: YY

# TODO: Write a regular expression that finds html tags in example.html and print them.
file = open("example.html", "r")
html_text = file.readlines()
file.close()

new_text = ''.join(html_text)
re.findall(r"<a\shref[^>]+>", new_text)

# TODO: Scrape a website and search for some things...
from bs4 import BeautifulSoup
import urllib2 
web_address = 'http://www.heinonline.org/HOL/Index?index=ustreaties/ustkav&collection=ustreaties'

Title = []
Force = []
SDN =[]
Country = []
Subject = []
Short = []
Desc = []
LastTIF = []
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
Extensions = soup.find_all('a', {'class': 'dt_link title'})
Links = []
prefix = 'http://www.heinonline.org/HOL/'
for ex in Extensions:
	suffix = str(ex['href'])
	whole = prefix+suffix
	Links.append(whole)
Links.reverse()
for link in Links:
	new_page = urllib2.urlopen(link)
	#new_page = urllib2.urlopen('http://www.heinonline.org/HOL/Index?index=ustreaties/kavs&collection=ustreaties')
	new_soup = BeautifulSoup(new_page)
	Extensions2 = new_soup.find_all('a', {'class': 'dt_link'})
	Links2 = []
	for ex2 in Extensions2:
		suffix2 = str(ex2['href'])
		whole2 = prefix+suffix2
		Links2.append(whole2)
	for link2 in Links2:
		new_page2 = urllib2.urlopen(link2)
		#new_page2 = urllib2.urlopen('http://www.heinonline.org/HOL/Page?handle=hein.ustreaties/kav00004&id=1&size=2&collection=ustreaties&index=ustreaties/kava#')
		new_soup2 = BeautifulSoup(new_page2)
		Ext = new_soup2.find_all('div', {'id' : 'hn_cit4'})
		text_chunk = str(Ext[0].get_text())
		number = re.findall(r'\d+', text_chunk)
		title = re.findall(r'KAV\s\d+', text_chunk)
		print title
		Title.append(title)
		prefix  ='http://www.heinonline.org/HOL/Metadata?type=KAV&number='
		suffix = '&collection=ustreaties'
		Final_Link = prefix+str(number[0])+suffix
		try:
			Final_page = urllib2.urlopen(Final_Link)
			Final_Soup = BeautifulSoup(Final_page)
			info = Final_Soup.find_all('td', {'valign':'top'})
			Info = []
			for line in info:
				Info.append(line.get_text())
			force = str(Info[3])
			force = re.findall(r'[A-Z]\w+', force)
			Force.append(force)
			sdn = str(Info[5])
			sdn = re.sub(r'\n\s+','',sdn)
			SDN.append(sdn)
			country = str(Info[7])
			country = re.sub(r'\n\s+','',country)
			Country.append(country)
			subject = str(Info[9])
			subject = re.sub(r'\n\s+','',subject)
			Subject.append(subject)
			short = str(Info[11])
			short = re.sub(r'\n\s+','',short)
			Short.append(short)
			desc = str(Info[13])
			desc = re.sub(r'\n\s+','',desc)
			Desc.append(desc)
			lasttif = str(Info[15])
			lasttif = re.findall(r'\d+', lasttif)
			LastTIF.append(lasttif)
		except:
			Force.append('NA')
			SDN.append('NA')
			Country.append('NA')
			Subject.append('NA')
			Short.append('NA')
			Desc.append('NA')
			LastTIF.append('NA')


