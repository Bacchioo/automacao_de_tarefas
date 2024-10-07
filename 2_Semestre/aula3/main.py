from selenium import webdriver

#cria um objeto do webDriver que vai manipular o Chrome
chrome = webdriver.Chrome()

#abre um endereço no navegador = get 
chrome.get('http://www.google.com')

#esperar digitar algo para fechar o navegador 
input('Aperte enter para terminar')