import time
import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from colorama import Fore, init, Back

init(autoreset=True)

options = webdriver.ChromeOptions ()
options.add_experimental_option ('elxcludeSwitches',['enable-logging'])

driver = webdriver.Chrome()
driver.maximize_window() 
error=0

#abrir sitio web
driver.get ("https://centroestant.com.ar/")
time.sleep(3)

#abre link muebles
puntoventa = driver.find_element(By.LINK_TEXT,"Puntos de Venta")
puntoventa.click()
pventa = driver.find_element(By.LINK_TEXT,"Puntos de Venta")
pventasNav = driver.find_element(By.XPATH,"//*[@id='menu-item-13488']/a").text

if "Puntos de Venta" == pventasNav:
    print (Fore.CYAN + "Visibilidad de Puntos de venta en el nav:" +Fore.GREEN+"PASS")
else:
    print (Fore.CYAN + "Visibilidad de Puntos de venta en el nav:" +Fore.RED+"FAIL")
    error+=1
    
time.sleep(2)

#abre cadenas oficiales
cadenaopen = driver.find_element(By.LINK_TEXT,"Cadenas Oficiales").click() 
time.sleep(2)
cadenaclose = driver.find_element(By.LINK_TEXT,"Cadenas Oficiales").click() 
time.sleep(2)



#abre tienda centro estant oficial
tiendaopen = driver.find_element(By.LINK_TEXT,"Tienda Centro Estant Oficial").click()
time.sleep(2)

#abre el link en otra pestaña
link= driver.find_element(By.LINK_TEXT,"https://tienda.centroestant.com.ar/")
link.send_keys(Keys.CONTROL + Keys.RETURN)
driver.switch_to.window(driver.window_handles[1])
time.sleep(7)
driver.close()

driver.switch_to.window(driver.window_handles[0])
time.sleep(2)

tiendaclose = driver.find_element(By.LINK_TEXT,"Tienda Centro Estant Oficial").click()
time.sleep(2)

logo = driver.find_element (By.ID,"logo")
logo.click()
time.sleep(3)


driver.close()
