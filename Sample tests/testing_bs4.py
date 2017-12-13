import requests, sys, webbrowser, bs4
res = requests.get('http://cee.umd.edu/faculty')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"lxml")
faculty = soup.find_all("div",{"id":"quicktabs-tabpage-faculty-0"})[0]
#print(faculty.find_all("div",{"class":"view-content"}))
for item in faculty.find_all("div",{"class":"views-row"}):
	#print(item)
	try:
		print(item.find_all("span")[0].text)
		print(item.find_all("div",{"class":"views-field views-field-field-title"})[0].text)
		print(item.find_all("div",{"class":"views-field views-field-field-address"})[0].text)
		print(item.find_all("span",{"class":"views-field views-field-field-phone"})[0].text)
		print(item.find_all("span",{"class":"views-field views-field-field-email"})[0].text)
	except Exception as e:
		print(e)
	print()