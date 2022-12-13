import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options


options = webdriver.ChromeOptions()
options.add_experimental_option('elxcludeSwitches',['enable-logging'])

driver = webdriver.Chrome()
driver.maximize_window() 
driver.get ("https://tienda.centroestant.com.ar/")
time.sleep(3)

compra = driver.find_element(By.ID,"menu-item-13478") 
compra.click()
time.sleep(2)

imagen = driver.find_element(By.ID,"image_185970984") 
imagen.click()
time.sleep(3)

flechader = driver.find_element(By.XPATH,"/html/body/div[2]/div/button[2]").click() 
time.sleep(2)
flechader = driver.find_element(By.XPATH,"/html/body/div[2]/div/button[2]").click()
time.sleep(2)
flechader = driver.find_element (By.XPATH,"/html/body/div[2]/div/button[2]").click()
time.sleep(2)
flechader = driver.find_element (By.XPATH,"/html/body/div[2]/div/button[2]").click()
time.sleep(2)
flechader = driver.find_element (By.XPATH,"/html/body/div[2]/div/button[2]").click()
time.sleep(2)

flechaizq = driver.find_element (By.XPATH,"/html/body/div[2]/div/button[1]").click()
time.sleep (2)
flechaizq = driver.find_element (By.XPATH,"/html/body/div[2]/div/button[1]").click()
time.sleep (2)

cerrarimg = driver.find_element (By.XPATH,"/html/body/div[2]/button").click()
time.sleep (2)

logo = driver.find_element (By.ID,"logo")
logo.click()
time.sleep (2)

driver.close ()

