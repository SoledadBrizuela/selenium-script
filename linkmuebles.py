import time
import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from colorama import Fore, init, Back

init(autoreset=True)

options = webdriver.ChromeOptions()
options.add_experimental_option('elxcludeSwitches',['enable-logging'])

driver = webdriver.Chrome()
driver.maximize_window()
error=0

#Abrir sitio web
driver.get("https://tienda.centroestant.com.ar/")
time.sleep(3)

#abrir link muebles
mueble = driver.find_element(By.LINK_TEXT,"Muebles")
mueble.click()
MueblesNav = driver.find_element(By.XPATH,"//*[@id='menu-item-12954']/a").text

if "Muebles" == MueblesNav:
    print (Fore.CYAN + "Visibilidad de Muebles en el nav:" +Fore.GREEN+"PASS")
else:
    print (Fore.CYAN + "Visibilidad de Muebles en el nav:" +Fore.RED+"FAIL")
    error+=1
    
time.sleep(3)

#seleccionar opcion alacenas
alacena = driver.find_element(By.LINK_TEXT,"Alacenas")
alacena.click()
productoAlacena = driver.find_element(By.XPATH,"//*[@id='woocommerce_product_categories-2']/ul/li/ul/li[1]").text

if "Alacenas" == productoAlacena:
    print (Fore.CYAN + "Visibilidad de la opcion Alacenas:" +Fore.GREEN+"PASS")
else:
    print (Fore.CYAN + "Visibilidad de la opcion Alacenas:" +Fore.RED+"FAIL")
    error+=1
    
time.sleep(2)

#selecciona un tipo de alacena
tipo = driver.find_element(By.LINK_TEXT,"Alacena 140")
tipo.click()
h1 = driver.find_element(By.XPATH,"//*[@id='product-14066']/div/div[1]/div/div[2]/h1" ).text


if "Alacena 140" == h1:
    print(Fore.CYAN + "Ingreso en el producto correcto:" +Fore.GREEN+"PASS")
else:
    print(Fore.CYAN + "Ingreso en el producto correcto:" +Fore.RED+"FAIL")
    error+=1

time.sleep(2)

#vuelve a la homepage
loguito = driver.find_element(By.ID,"logo")
loguito.click()
time.sleep(3)
    
driver.close()

