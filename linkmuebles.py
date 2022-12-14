import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options


options = webdriver.ChromeOptions()
options.add_experimental_option('elxcludeSwitches',['enable-logging'])

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tienda.centroestant.com.ar/")
time.sleep(3)

categoria = driver.find_element(By.ID,"menu-item-12954")
categoria.click()
time.sleep(3)

producto = driver.find_element(By.LINK_TEXT,"Alacenas")
producto.click()
time.sleep(2)

tipo = driver.find_element(By.LINK_TEXT,"Alacena 140")
tipo.click()
time.sleep(2)

logo = driver.find_element(By.ID,"logo")
logo.click()
time.sleep(3)

driver.close()
print("OK")