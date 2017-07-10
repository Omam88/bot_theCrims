import config
from robobrowser import RoboBrowser
from selenium import webdriver
#from bs4 import BeautifulSoup

#**********IGNORE THIS CODE, I'M DO TO WHEN I EXECUTE WITH ROBOBROWSER, BUT DOESN'T DIFFERENCE TO THE SELENIUM CODE.***********

#Define um navegador, e faz login no TheCrims através do formulário do facebook
br = RoboBrowser(   
		history=True,
        user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0',
        parser='html.parser'
    )
br.open("https://www.thecrims.com/login/facebook")
form = br.get_form(id='login_form')
form['email'] = config.DATACOUP_USERNAME
form['pass'] = config.DATACOUP_PASSWORD
br.submit_form(form)
action_menu = str(br.find(class_='action_menu'))	#Encontra a classe que contém todos os links para os menus do TheCrims, e a transforma em string e faz referência para action_menu.

#br.follow_link(config.MudarPage(config.GetLinksVar(action_menu)[0]))	#Faz um clique de mudança de página através do navegador, passando como parâmetro um link BeautifulSoup.
formsInRoubo = br.find_all('form')	#Encontra todos formulários na página de roubos e retorna em bs4 result
formToRoubo = formsInRoubo[1]
formuu = br.get_forms()[1]

def GetFormsRouboPage(x):
	formsInRouboPage = list(range(len(x)))	#Cria uma array com o tamanho de formsInRoubo
	for i in range(len(x)):
		formsInRouboPage[i] = br.get_form(x[i])	#Define todos os formulários de roubo Solo em robobrowser.form e faz referência para formsInRouboPage.
	return formsInRouboPage

formTeste = GetFormsRouboPage(formsInRoubo)[1]

print(action_menu)










'''
rouboSolo = br.find(id='single-robbery-select')
optionRouboSolo = br.find('option select')



forms = br.select("td form")
Analgesicos = br.find('$15')
formComprar['quantity'] = 
print(forms[1])
print(Analgesicos)


formLSD = br.get_form(config.TransformForm(config.formLSD))
print(type(form))
print(type(formLSD))
print(len(br.find_all("form", {"class":"ng-pristine.ng-valid.ng-empty.ng-valid-maxlength.ng-touched"})))
'''
