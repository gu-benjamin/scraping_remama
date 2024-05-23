import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.instagram.com/accounts/login/"

driver.get(url)
time.sleep(2)

username = "dieckgenios"
senha = "A_lBiKc9MEFT8-9"

driver.find_element(By.NAME, "username").send_keys(username)

time.sleep(2)

driver.find_element(By.NAME, "password").send_keys(senha)

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5)

pesquisa = "remamadragaorosa"
driver.find_element(By.CSS_SELECTOR, "[aria-label='Pesquisa']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "[aria-label='Entrada da pesquisa']").send_keys(pesquisa)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "[href='/remamadragaorosa/']").click()
time.sleep(3)

scroll_pause_time = 2  # pausa no tempo do scroll para acompanhar o processo
screen_height = driver.execute_script("return window.screen.height;")  # pega o tamanho da pagina
i = 1
links_set_posts = set()

while True:
  # desce a pagina no tamanho de uma tela por vez
  driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
  i += 1
  time.sleep(scroll_pause_time)

  temp_links_posts = driver.find_elements(By.CSS_SELECTOR, "a[role='link'][href^='/p/']")[:]
  temp_links_reels = driver.find_elements(By.CSS_SELECTOR, "a[role='link'][href^='/reel/']")[:]

  for link_post in temp_links_posts:
    links_set_posts.add(link_post.get_attribute('href'))
    
  for link_reel in temp_links_reels:
    links_set_posts.add(link_reel.get_attribute('href'))
    
  temp_links_posts.clear()

  print(len(links_set_posts))

  # atualize a altura da rolagem sempre que rolar, pois a altura da rolagem pode mudar depois que rolamos a página
  scroll_height = driver.execute_script("return document.body.scrollHeight;")
  # interrompa o loop quando a altura que precisamos rolar for maior que a altura total da rolagem
  if (screen_height) * i > scroll_height:
    try:   
      login_modal = driver.find_element(By.CSS_SELECTOR, "div[role='dialog']")
      driver.execute_script("document.querySelector('body > div:nth-child(38) > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9p._ab9z._aba9._abch._abck.x1vjfegm._abcm > div').click()")
      time.sleep(1)
    except NoSuchElementException as error:
      print('Fim dos reels!')
      break

links_posts = list(links_set_posts)

curtidas = []
comentarios = []
datas_publicacoes = []
legendas = []
links_postagem = [] # Caso queira rodar novamente o script, descomentar esta linha para adicionar o link da postagem ao dataframe
tipo_post = []

print(f'Quantidade de posts: {len(links_posts)}')
n_post = 1

for link in links_posts:
  try:  
    driver.get(link)
    time.sleep(2)
    print(f'\nPost {n_post}\n')
    # Acessando as tags meta do DOM de cada reel do instagram do remama, onde contém as informações da publicação
    meta_reel_info = driver.find_element(By.NAME, 'description').get_attribute('content').split('-')
    meta_reel_numbers = meta_reel_info[0].replace(',','').split()

    # Extraindo separadamente informações de curtidas, comentários, legenda do post e data de publicação
    curtida = int(meta_reel_numbers[0]) if meta_reel_numbers[1] == 'likes' else int(meta_reel_numbers[2])
    comentario = int(meta_reel_numbers[2]) if meta_reel_numbers[-1] == 'comments' else int(meta_reel_numbers[0])
    data_publicacao = meta_reel_info[1].split(':')[0].split('em ')[1]
    # Formatando data da publicação para o formato correto
    data_formatada = datetime.strptime(data_publicacao, "%B %d, %Y").strftime("%d/%m/%Y")
    legenda = driver.find_element(By.CSS_SELECTOR, "meta[property='og:title']").get_attribute('content').replace('Remama Dragão Rosa Oficial no Instagram: ', '')

    print(f'Curtidas: {curtida}\nComentarios: {comentario}\nData: {data_formatada}\nLegenda: {legenda[:10]}...\nLink: {link}\nTipo: {'Post' if link[25:28] == '/p/' else 'Reel'}')
    # Adicionando informações do reel visitado nas listas
    curtidas.append(curtida)
    comentarios.append(comentario)
    datas_publicacoes.append(data_formatada)
    legendas.append(legenda)
    links_postagem.append(link) # Caso queira rodar novamente o script, descomentar esta linha para adicionar o link da postagem ao dataframe
    tipo_post.append('Post' if link[25:28] == '/p/' else 'Reel')

    #   print(f'{len(curtidas)} {len(comentarios)} {len(datas_publicacoes)} {len(legendas)}')

    n_post += 1
    # Indo pro próximo reel
    driver.back()
        
  except NoSuchElementException as error:
    curtidas.append('-')
    comentarios.append('-')
    datas_publicacoes.append('-')
    legendas.append('-')
    links_postagem.append('-') 
    tipo_post.append('-')

data = {
  'Curtidas': curtidas,
  'Comentários': comentarios,
  'Datas de publicação': datas_publicacoes,
  'Legendas': legendas,
  'Links dos posts': links_postagem, # Caso queira rodar novamente o script, descomentar esta linha para adicionar o link da postagem ao dataframe
  'Tipo de post': tipo_post
}

dados_post = pd.DataFrame(data)
print(dados_post)
dados_post.to_excel('dados_posts_remama.xlsx')