#Bibliothèque selenium
from selenium import webdriver
import time
import os


#Introduction necessaire au module selenium
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito") #permet la navigation privée
chromeOptions.add_argument("--start-maximized")  #pour ouvrir la page en grand 
#prefs={"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096 }
#option.add_experimental_option('prefs', prefs)
#browser = webdriver.Chrome(executable_path=str(os.getcwd())+"\chromedriver", options=option) #!!! Executable à télécharger et path à changer
browser = webdriver.Chrome(executable_path=r"C:\Users\Maxime\Documents\Formation\Scrapping\chromedriver.exe", options=chromeOptions)


plat="Tarte aux fraises"
print('Recette : '+plat)


browser.get('https://www.marmiton.org/')



barre_recherche = browser.find_element_by_xpath('//input[@class="recipe-home-search__search-bar-input"]')
barre_recherche.send_keys(plat)

#Mieux !!!! barre_recherche = browser.find_element_by_xpath('//form[@id="recipe-home-search__form"]/div[1]/input[1]')

button=browser.find_element_by_xpath('//form[@id="recipe-home-search__form"]/div[1]/button[1]')
button.click()


plat_separe=plat.lower().split(' ')
plat_tiret=""
for plat_i in plat_separe:
    plat_tiret+=plat_i+'-'
plat_tiret=plat_tiret[:-1]

browser.get('https://www.marmiton.org/recettes/recherche.aspx?aqt='+plat_tiret)


recette=browser.find_element_by_xpath('//div[@class="recipe-results "]/div[1]/a[1]')
lien_recette=recette.get_attribute('href')

browser.get(lien_recette)

time.sleep(3)

temps=browser.find_element_by_xpath('//div[@class="recipe-infos__total-time"]/span[2]').text
print('Temps de préparation total : '+temps)

liste_ingredients=browser.find_elements_by_xpath('//ul[@class="recipe-ingredients__list"]/li/div')
for ingredient in liste_ingredients:
    print(ingredient.text)






#Scroll infini
SCROLL_PAUSE_TIME = 1.5
last_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    time.sleep(SCROLL_PAUSE_TIME)

    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



