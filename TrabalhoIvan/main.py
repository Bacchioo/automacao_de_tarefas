#importar modulos
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import wget

planilha = pd.DataFrame(columns=['Nome', 'Preco', 'Imagem'])

#criar um objeto para manipular o navegador
chrome = webdriver.Chrome()

#abrir uma página no chrome
chrome.get('https://www.kabum.com.br/perifericos/-mouse-gamer/com-fio')

#Procurar pelo elemento que possui o nome
elementNome = chrome.find_elements(By.CLASS_NAME, "sc-d79c9c3f-0")

#Procurar pelo elemento que possui o preco
elementPreco = chrome.find_elements(By.CLASS_NAME, "sc-57f0fd6e-2")

#procurar pela imagem
elementImage = chrome.find_elements(By.CLASS_NAME, "imageCard")
contador = 0

while contador < 10:
    enderecoImage = elementImage[contador].get_attribute('src')

    #cria um novo nome para a imagem
    nomeProduto = "RATOS" + str(contador)
    extensaoImg = enderecoImage.split(".")[-1]
    nomeImagem = nomeProduto + "." + extensaoImg
    ondeSalvar = "TrabalhoIvan\\img\\" + nomeImagem

    wget.download(enderecoImage, ondeSalvar)

    print("\nNome: ", elementNome[contador].text)
    print("Preço: ", elementPreco[contador].text)
    print("\n")

    #adiciona os dados na planilha
    planilha.loc[contador] = [elementNome[contador].text, elementPreco[contador].text, nomeImagem]

    #incremento para a parada do while
    contador = contador + 1

ondeSalvarPlan = "TrabalhoIvan"

#salva a planilha em formato excel
planilha.to_excel("TrabalhoIvan\\RATOS.xlsx", index = True)



#mantém a página aberta
input('Pressione enter para terminar')