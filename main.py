import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.instagram.com/remamadragaorosa/reels/'

driver.get(url)

time.sleep(5)
scroll_pause_time = 3  # pausa no tempo do scroll para acompanhar o processo
screen_height = driver.execute_script("return window.screen.height;")  # pega o tamanho da pagina
i = 1
reels = []
links_reels = []
descs_reels = []

while True:
    # desce a pagina no tamanho de uma tela por vez
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)

    reels = driver.find_elements(By.CLASS_NAME, '_abq3')[:] 
    links_reels = [reel.find_element(By.TAG_NAME, 'a').get_attribute('href') for reel in reels][:]
    print(len(reels))
    print(len(links_reels))

    # atualize a altura da rolagem sempre que rolar, pois a altura da rolagem pode mudar depois que rolamos a página
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    # interrompa o loop quando a altura que precisamos rolar for maior que a altura total da rolagem
    if (screen_height) * i > scroll_height:
        break


for link in links_reels:
    driver.get(link)
    time.sleep(3)
    meta_reel = driver.find_element(By.NAME, 'description')
    desc_reel = meta_reel.get_attribute('content')
    print(desc_reel)
    descs_reels.append(desc_reel)
    driver.back()

print(descs_reels)
