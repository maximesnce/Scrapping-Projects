#Bibliothèque selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

#Dataframe
import pandas as pd


#Introduction necessaire au module selenium
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito") #permet la navigation privée
chromeOptions.add_argument("--start-maximized")  #pour ouvrir la page en grand 
#prefs={"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096 }
#chromeOptions.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path=r"C:\Users\Maxime\Documents\Formation\Scrapping\chromedriver.exe", options=chromeOptions) #!!! Executable à télécharger et path à changer


browser.get('https://old-athena.juniorcs.fr/login.php') #on met le site qu'on veut et .get c'est pour aller sur une page


#Connexion
login = 'user_name'
mdp = 'password'

username = browser.find_element_by_xpath("//form[@method='post']/div[1]/div[1]/input") 
username.send_keys(login)

password = browser.find_element_by_xpath("//form[@method='post']/div[2]/div[1]/input")
password.send_keys(mdp)

connexionInButton = browser.find_element_by_xpath("//form[@method='post']/div[3]/div[1]/input")
connexionInButton.click()



#Obtention des statistiques générales de la JE

données_JCS = pd.DataFrame(columns = ['Nombre d études signées', 'JEH', 'CA', 'Budget moyen'])

statistiques_button = browser.find_element_by_xpath("//ul[@id = 'main_menu']/li[5]/a")
statistiques_button.click()

information_generale = browser.find_element_by_xpath("//div[@id = 'content']/div[1]/p[1]").text
infos = re.split('[:\n]',information_generale)


données_JCS = données_JCS.append({'Nombre d études signées' : infos[1], 'JEH' : infos[3], 'CA' : infos[5], 'Budget moyen' : infos[11]} ,ignore_index = True)




#Statistiques du Chef de Projet

liens=[]
données_missions = pd.DataFrame(columns = ['Réf', 'Signé', 'JEH', 'CA signé'])

browser.get('https://old-athena.juniorcs.fr/login.php')

missions = browser.find_elements_by_xpath("//div[@class = 'tricol etudes']/p/a")
for mission in missions :
    liens.append([mission.text, mission.get_attribute('href')])


for lien in liens :
    browser.get(lien[1])
    try : 
        chiffres = browser.find_element_by_xpath("//div[@class = 'droite']/p[1]").text
        chiffre = re.split('[:\n]', chiffres)
        données_missions = données_missions.append({'Réf' : lien[0], 'Signé' : 'Oui', 'JEH' : chiffre[9], 'CA signé' : chiffre[1]}, ignore_index = True)
    except :
        données_missions = données_missions.append({'Réf' : lien[0], 'Signé' : 'Non', 'JEH' : 0, 'CA signé' : 0}, ignore_index = True)
        


