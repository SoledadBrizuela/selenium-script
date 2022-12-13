import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options


options = webdriver.ChromeOptions ()
options.add_experimental_option ('elxcludeSwitches',['enable-logging'])

driver = webdriver.Chrome()
driver.maximize_window() 
driver.get ("https://centroestant.com.ar/")
time.sleep(3)

puntoventa = driver.find_element(By.ID,"menu-item-13488")
puntoventa.click()
time.sleep(3)


cadenaopen = driver.find_element(By.XPATH,"//*[@id='col-1974088881']/div/div/div[1]/a/button").click() 
time.sleep(2)
cadenaclose= driver.find_element(By.XPATH,"//*[@id='col-1974088881']/div/div/div[1]/a/button").click() 
time.sleep(2)

tiendaopen = driver.find_element(By.XPATH,"//*[@id='col-1974088881']/div/div/div[2]/a/button").click()
time.sleep(2)
tiendaclose= driver.find_element(By.XPATH,"//*[@id='col-1974088881']/div/div/div[2]/a/button").click()
time.sleep(2)

logo = driver.find_element (By.ID, "logo")
logo.click()
time.sleep (2)

driver.close()