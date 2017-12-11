import requests, sys, webbrowser, bs4
res = requests.get('http://cee.umd.edu/faculty')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"lxml")

for faculty in soup.find_all("div",{"class":"view-content"}):
	try:
		print(faculty.div.span.a.text)
	except:
		pass