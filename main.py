import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.instagram.com/remamadragaorosa/'

driver.get(url)
time.sleep(2)

artigo = driver.find_elements(By.TAG_NAME, 'article')

print(artigo)
