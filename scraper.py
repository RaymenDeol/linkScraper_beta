import requests, bs4

def getURL() :
	url = input("Enter URL (Use the following format: 'http(s)://google.com')   ")
	return url

def makeRequest(url) :
	while True:
		
		try:
			response = requests.get(url)
			response.raise_for_status()
		except requests.exceptions.RequestException as e:
			print(e)
			print('ERROR! Please ensure formatting is correct and the web server is online.')
			url = getURL()
			continue
		break	
	return response

def getLinks(pageContent):
	soupObj = bs4.BeautifulSoup(pageContent.text, "html5lib")
	n = 0
	list = []
	for i in soupObj.find_all('a'):
		list.append(i.get('href'))
	return list
		
website = getURL()
response = makeRequest(website)
links = getLinks(response)
print(links)