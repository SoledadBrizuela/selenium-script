import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions ()
options.add_experimental_option ('elxcludeSwitches',['enable-logging'])

driver = webdriver.Chrome()
driver.maximize_window() 
driver.get ("https://centroestant.com.ar/")
time.sleep(3)

puntoventa = driver.find_element(By.ID,"menu-item-13488")
puntoventa.click()
time.sleep(2)


cadenaopen = driver.find_element(By.LINK_TEXT,"Cadenas Oficiales").click() 
time.sleep(2)
cadenaopen = driver.find_element(By.LINK_TEXT,"Cadenas Oficiales").click() 
time.sleep(2)

tiendaopen = driver.find_element(By.LINK_TEXT,"Tienda Centro Estant Oficial").click()
time.sleep(2)

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
print("OK")