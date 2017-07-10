from  selenium import webdriver
import config
import re
import time
import winsound


url = 'https://www.thecrims.com/login/facebook'
nroubo = 0	#Just a variable to identify the number of times that bot do it.
staminapa = 25 #number of minimum stamina to enter on loop bot. It's based in wich assalt you want to do with 100% success rate.
vicioP = 3	#number of minimum addiction to go to the hospital
numberRodadas = 10	#It's the number of each time that finish one goals, exemple.: 4 assalts and recover stamina is a goals. Times that the bot come again.
roubos = 0	#Number of assalts done at sound beep in window.

driver = webdriver.PhantomJS()
driver.get(url)

email = driver.find_element_by_name('email')
senha = driver.find_element_by_name('pass')
email.send_keys(config.DATACOUP_USERNAME)
senha.send_keys(config.DATACOUP_PASSWORD)
#form = driver.find_element_by_xpath("//form[@id='login_form']")
driver.find_element_by_name('login').click()


def VerificarCaptcha():	#This pick if captcha is show on or off, and make a sound to identify that. 
	vercaptcha = driver.find_element_by_tag_name('h1')
	if (vercaptcha.text == 'PATRULHA POLICIAL'):	#Change this input by the your language, i'm brazilian so if you be another country, change to your country.
		print('Número de roubos' + ': ' + str(roubos))
		winsound.Beep(1000, 1000)
		driver.close()
'''
action_menu = driver.find_elements_by_tag_name('li')
for i in range(len(action_menu)):	Is the way that I choose 41 or 42. Must verify(print) before click it.
	print (action_menu[i].text)
	print(i)
'''

def AtualizaValores():	#Refresh the values of stamina and addiction of player, before bot starts.
	stamina = driver.find_element_by_id('user-profile-stamina')
	staminaN = int(stamina.text[10:-1])
	vicio = driver.find_element_by_id('user-profile-addiction')
	vicioN = int(vicio.text[7:-1])
	return (staminaN, vicioN)

staminaN, vicioN = AtualizaValores()

while (nroubo < numberRodadas):

	if(staminaN >= staminapa):
		action_menu = driver.find_elements_by_tag_name('li')	#Change to assalt
		action_menu[41].click()
		print('Entrando na página de roubos...')
		time.sleep(2)
		VerificarCaptcha()
		element = driver.find_element_by_xpath("//select[@id='single-robbery-select']")
		all_options = element.find_elements_by_tag_name("option")
		rouboCerto = int(config.EscolherRoubo(all_options))
		print('Stamina' + ': ' + str(staminaN))
		time.sleep(2)

	while (staminaN >= staminapa):
		all_options = element.find_elements_by_tag_name("option")
		all_options[rouboCerto].click()
		print('Roubo escolhido' + ": " + str(rouboCerto))
		driver.find_element_by_id('single-robbery-submit').click()
		print('Roubando...')
		time.sleep(5)
		roubos = roubos + 1
		VerificarCaptcha()
		staminaN, vicioN = AtualizaValores()
		print('Stamina' + ': ' + str(staminaN))

	if(staminaN < staminapa):
		action_menu = driver.find_elements_by_tag_name('li') #Must define another time 
		action_menu[42].click()
		print('Entrando na página de Vida Noturna...')
		time.sleep(5)
		VerificarCaptcha()
		action_menuU = driver.find_elements_by_xpath("//input[@value='Entrar']")
		time.sleep(3)
		action_menuU[1].click()
		print('Entrando no puteiro pré-determinado...')
		VerificarCaptcha()
		sair = driver.find_element_by_xpath("//a[@href='#']")
		action_menuUU = driver.find_elements_by_xpath("//input[@value='Comprar']")
		time.sleep(1)
		action_menuUU[8].click()
		time.sleep(2)
		staminaN, vicioN = AtualizaValores()
		print('Stamina' + ': ' + str(staminaN))
		print('vicio' + ': ' + str(vicioN))
		sair.click()

	if(vicioN >= vicioP):
		action_menu = driver.find_elements_by_tag_name('li')	#Change to hospital
		action_menu[49].click()
		print('Entrando na página do hospital...')
		time.sleep(3)
		driver.find_element_by_xpath("//input[@value='Desintoxicar por dinheiro']").click()
		print('Desintoxicação completa!!')
		staminaN, vicioN = AtualizaValores()
		print('vicio' + ': ' + str(vicioN))

	nroubo = nroubo + 1
	staminaN, vicioN = AtualizaValores()
	print(nroubo)
	time.sleep(5)

driver.close()
