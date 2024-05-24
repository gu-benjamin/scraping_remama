# Web Scraping Remama

<!-- <div> 
  <img align='center' style='width: 300px' src='assets/img/Logo.svg'/>
</div> -->

## Tabela de Conteúdo

- [Objetivo](#objetivo)
- [Tecnologias](#tecnologias)
- [Como clonar](#como-clonar)
- [Como inicializar o projeto](#como-inicializar-o-projeto)
- [Inicializar](#inicializar)


## Objetivo

O objetivo principal deste projeto está voltado a extração de informações de posts de uma página do Instagram, sendo coletada quantidade de curtidas e comentários, data da publicação, legenda e link da postagem e tipo de post(Post ou Reel).   

## Tecnologias

<div>
  <img src='https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white'/>   
  <!-- <img src='https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white'/>   
  <img src='https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white'/>   
  <img src='https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white'/>    -->
</div>

## Como Clonar

Para clonar o repositório de Web Scraping, você pode seguir os passos abaixo:

1. No terminal, clone o projeto usando este comando:
```bash
git clone https://github.com/gustavinxd/scraping_remama.git
```
2. Depois de clonado, acesse o diretório do projeto usando o comando a seguir
```bash
cd scraping_remama
```

## Como inicializar o projeto

Antes de inicializar o projeto, deve se conferir se possui os seguintes pré requisitos para inicializa-lo:

1. Certifique-se de ter o Git instalado em sua máquina. Você pode verificar se o Git está instalado executando o seguinte comando no terminal:

```bash
git --version
```

Se o Git não estiver instalado, você pode baixá-lo em https://git-scm.com/.

2. Python e depedências: Você precisará do Python instalado na sua máquina e as bibliotecas do projeto.

### Inicializar

Após conferir os pré-requisitos e estar no diretório do projeto, você deve seguir os seguintes passos:

1. Baixe os módulos do projeto executando o seguinte comando:
   
```bash
pip install pandas
```
```bash
pip install selenium
```
```bash
pip install openpyxl
```

2. Após instalar os módulos, execute o projeto com o comando:
   
```bash
python main.py
```
Ao executar o comando, o código iniciará acessando o user informado e acessará a página escolhida para iniciar a extração das informações.

