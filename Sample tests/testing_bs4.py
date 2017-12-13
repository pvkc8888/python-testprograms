import requests, sys, webbrowser, bs4,csv

res = requests.get('http://cee.umd.edu/faculty')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"lxml")
filename = 'Civil_Contacts.csv'
with open('Civil_Contacts.csv', 'wb') as new_file:
	fieldnames = ['Name','Address','Contact number','email id']
	writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter = "\t")
	writer.writeheader()
	faculty = soup.find_all("div",{"id":"quicktabs-tabpage-faculty-0"})[0]

	for item in faculty.find_all("div",{"class":"views-row"}):
		try:
			print(item.find_all("span")[0].text)
			writer.writerow(item.find_all("span")[0].text)

		except:
			writer.writerow(item.find_all("span")[0].text)
		try:	
			print(item.find_all("div",{"class":"views-field views-field-field-title"})[0].text)
			writer.writerow(item.find_all("div",{"class":"views-field views-field-field-title"})[0].text)
		except:
			writer.writerow(item.find_all("span")[0].text)
		try:	
			print(item.find_all("div",{"class":"views-field views-field-field-address"})[0].text)
			writer.writerow(item.find_all("div",{"class":"views-field views-field-field-address"})[0].text)
		except:
			writer.writerow(item.find_all("span")[0].text)
		try:
			print(item.find_all("span",{"class":"views-field views-field-field-phone"})[0].text)
			writer.writerow(item.find_all("span",{"class":"views-field views-field-field-phone"})[0].text)
		except:
			writer.writerow(item.find_all("span")[0].text)
		try:
			print(item.find_all("span",{"class":"views-field views-field-field-email"})[0].text)
			writer.writerow(item.find_all("span",{"class":"views-field views-field-field-email"})[0].text)
		except:
			writer.writerow(item.find_all("span")[0].text)
		print()
writer.close()