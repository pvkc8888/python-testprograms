import requests, sys, webbrowser, bs4
res = requests.get('http://cee.umd.edu/faculty')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

linkElems = soup.find_all("div",{"class":"view view-faculty view-id-faculty view-display-id-page view-dom-id-8924432f221617777408fb3bc0dc79da"})
for items in linkElems:
	try:
		print(items.contents[1].text)
	except:
		pass	