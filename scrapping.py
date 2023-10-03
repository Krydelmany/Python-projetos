senha_escondida = "159951123"
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ra = "215656"
pas = senha_escondida

service = Service()

options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(service=service, options=options)

url = "https://www.unisalesiano.com.br/salaEstudo/alunos/"
driver.get(url)


# Seleciona a unidade de Araçatuba
driver.find_element(By.XPATH, '/html/body/main/div[3]/div[1]/div[2]/div/form/div[1]/div[2]/div/input').click()
driver.find_element(By.XPATH, '/html/body/main/div[3]/div[1]/div[2]/div/form/div[1]/div[2]/div/ul/li[3]/span').click()

# Preencha o campo RA
ra_input = driver.find_element(By.NAME, 'ra')
ra_input.send_keys(ra)

# Preencha o campo senha
senha_input = driver.find_element(By.NAME, "senha")
senha_input.send_keys(pas)

# Entra 
entrar = driver.find_element(By.XPATH, '/html/body/main/div[3]/div[1]/div[2]/div/form/div[4]/button')
entrar.click()

# Entra no ava
url_ava = 'https://www.unisalesiano.com.br/salaEstudo/libs/soa/loginAva.php'
driver.get(url_ava)
