#from bs4 import BeautifulSoup
import re

DATACOUP_USERNAME = ''	#Email
DATACOUP_PASSWORD = ''	#PassWord

'''
linksTag_a = '', '', '<a href="https://www.thecrims.com/drugdealer"></a>'
#linksTag_a = 0-roubo, 1-boate, 2-traficante

#Pega um link dentro da tag <a> do html e transforma/extrai em um link BeautifulSoup
def MudarPage(x):
	tagParaPage = x
	pageB = BeautifulSoup(tagParaPage, "html.parser")
	page = pageB.a
	return page

def GetLinksVar(x):
	action_menu = x
	links = re.findall(r'data-link=..\w+', action_menu)
	linksToFollow = list(range(len(linksTag_a)))
	linksToFollow[0] = '<a href="https://www.thecrims.com/' +links[1][12:] +'"></a>'
	linksToFollow[1] = '<a href="https://www.thecrims.com/' +links[2][12:] +'"></a>' 
	for i in range(2, len(linksTag_a)):
		linksToFollow[i] = linksTag_a[i]
	return linksToFollow

def GetLinksVars(x):
	action_menu = x
	links = re.findall(r'data-link=..\w+', action_menu)
	linksToFollow = list(range(len(linksTag_a)))
	linksToFollow[0] = 'https://www.thecrims.com/' +links[1][12:]
	linksToFollow[1] = 'https://www.thecrims.com/' +links[2][12:] 
	for i in range(2, len(linksTag_a)):
		linksToFollow[i] = linksTag_a[i]
	return linksToFollow
'''	
#The methods under is another project, i'm trying do this bot wih robobrowser library, but this option is limited. So, i'm do with selenium.


def EscolherRoubo(x):
	listaRoubos = x
	listaRoubosRE = list(range(len(listaRoubos)))
	listaRoubosINT = list(range(len(listaRoubos) + 1))
	for i in range(len(listaRoubos)):
		if (i == 0):
			listaRoubosRE[i] = 100
		else:
			listaRoubosRE[i] = str(re.findall(r'SP:.\w+', listaRoubos[i].text))[6:-2]
			listaRoubosINT[i - 1] = int(listaRoubosRE[i])
			if(listaRoubosINT[i - 1] == 100):
				rouboapto = i
	return rouboapto