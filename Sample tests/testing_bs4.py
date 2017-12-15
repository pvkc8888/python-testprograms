import requests, sys, webbrowser, bs4,csv

res = requests.get('http://www.enme.umd.edu/faculty')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"lxml")
filename = 'Civil_Contacts.csv'
with open('Civil_Contacts.csv', 'w') as new_file:
	fieldnames = ['Name','Field title','Address','Contact number','email id']
	writer = csv.DictWriter(new_file, delimiter = ",",fieldnames = fieldnames)
	writer.writeheader()
	faculty = soup.find_all("div",{"id":"quicktabs-tabpage-faculty-0"})[0]

	for item in faculty.find_all("div",{"class":"views-row"}):
		try:
			print(item.find_all("span")[0].text)
			name = item.find_all("span")[0].text

		except:
			name = "No name given"
		try:	
			print(item.find_all("div",{"class":"views-field views-field-field-title"})[0].text)
			field = item.find_all("div",{"class":"views-field views-field-field-title"})[0].text
		except:
			field = "None"
		try:	
			print(item.find_all("div",{"class":"views-field views-field-field-address"})[0].text)
			address = item.find_all("div",{"class":"views-field views-field-field-address"})[0].text
		except:
			address = "None"
		try:
			print(item.find_all("span",{"class":"views-field views-field-field-phone"})[0].text)
			cno = item.find_all("span",{"class":"views-field views-field-field-phone"})[0].text
		except:
			cno = "None"
		try:
			print(item.find_all("span",{"class":"views-field views-field-field-email"})[0].text)
			email = item.find_all("span",{"class":"views-field views-field-field-email"})[0].text
		except:
			email = "None"
		writer.writerow({"Name":name,"Field title":field,"Address":address,"Contact number":cno,"email id":email})
		print()
#writer.close()