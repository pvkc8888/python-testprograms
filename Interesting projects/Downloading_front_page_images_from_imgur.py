import bs4,urllib,os,re,os.path,requests

def downloadimage(url,filename):
	urllib.request.urlretrieve(url,filename)

changeurl = re.compile(r'https://i.imgur.com/(.*).jpg')


folder = os.getcwd()
finalfolder = os.path.join(folder,'imgur top page')
if not os.path.exists(finalfolder):
	os.makedirs(finalfolder)
os.chdir(finalfolder)
res = requests.get('https://imgur.com/')
res.raise_for_status()
i = 1
soup = bs4.BeautifulSoup(res.text)
Firstpage = soup.find_all("div",{"class":"posts br5 first-child"})[0]
for item in Firstpage.find_all("div",{"class":"post"}):
	url = 'https:'+item.find('img')['src']
	idimage = changeurl.findall(url)
	idimage  = idimage[0]
	url = 'https://i.imgur.com/'+idimage[0:len(idimage)-1]+'.jpg' 
	filename = str(i) +'.jpeg'
	downloadimage(url,filename)
	i = i+1
