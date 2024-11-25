#importar modulos
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import wget

contador = 0
i = 0

planilha = pd.DataFrame(columns=['Nome', 'Preco','Descrição','Autor', 'Imagem',])

#criar um objeto para manipular o navegador
chrome = webdriver.Chrome()

#abrir uma página no chrome
chrome.get('https://www.editoradodireito.com.br/universitarios')


#Procurar pelo elemento que possui o nome
elementNome = chrome.find_elements(By.CLASS_NAME, "base")

#Procurar pelo elemento que possui o preco
elementPreco = chrome.find_elements(By.CLASS_NAME, "price")

elementAutor = chrome.find_elements(By.CLASS_NAME, "authors")

elementDescricao = chrome.find_elements(By.CLASS_NAME, "description")

#procurar pela imagem
elementImage = chrome.find_elements(By.CSS_SELECTOR, "fotorama__img")
#enderecoImage = elementImage[contador].get_attribute('src')


#print("Link: ", elementlink[contador].text)
print("Nome: ", elementNome.text)
print("Preço: ", elementPreco.text)
print("Autor: ", elementAutor.text)
print("Sinopse: ", elementDescricao.text)
print("\n")

#nomeProduto = "livros" + str
#extensaoImg = enderecoImage.split(".")[-1]
#nomeImagem = nomeProduto + "." + extensaoImg
#ondeSalvar = "TrabalhoIvan\\img\\" + nomeImagem + ".png"

#wget.download(enderecoImage, ondeSalvar)

while contador < 36:
#    enderecoImage = elementImage[contador].get_attribute('src')

    #cria um novo nome para a imagem
#    nomeProduto = "RATOS" + str(contador)
#    extensaoImg = enderecoImage.split(".")[-1]
#    nomeImagem = nomeProduto + "." + extensaoImg
#    ondeSalvar = "TrabalhoIvan\\img\\" + nomeImagem


    #print("\nLink: ", elementlink[contador].text)

    #adiciona os dados na planilha
#    planilha.loc[contador] = [elementNome[contador].text, elementPreco[contador].text, nomeImagem]

    #incremento para a parada do while
    contador = contador + 1

#ondeSalvarPlan = "TrabalhoIvan"

#salva a planilha em formato excel
#planilha.to_excel("TrabalhoIvan\\RATOS.xlsx", index = True)



#mantém a página aberta
input('Pressione enter para terminar')