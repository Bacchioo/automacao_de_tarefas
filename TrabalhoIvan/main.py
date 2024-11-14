#importar modulos
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import wget

planilha = pd.DataFrame(columns=['Número', 'Nome', 'Altura', 'Imagem'])

#criar um objeto para manipular o navegador
chrome = webdriver.Chrome()

#abrir uma página no chrome
chrome.get('https://sg.portal-pokemon.com/play/pokedex/0001')

contador = 0

while contador < 10:

    #Procurar pelo elemento que possui o código do pokemon
    elementNumero = chrome.find_element(By.CLASS_NAME, "pokemon-slider__main-no")

    #Procurar pelo elemento que possui o nome do pokemon
    elementNome = chrome.find_element(By.CLASS_NAME, "pokemon-slider__main-name")

    #procura pela altura do pokemon
    elementAltura = chrome.find_element(By.CSS_SELECTOR, ".pokemon-info__height .pokemon-info__value")

    #procurar pela imagem
    elementImage = chrome.find_element(By.CLASS_NAME, "pokemon-img__front")
    enderecoImage = elementImage.get_attribute('src')

    #cria um novo nome para a imagem
    urlNavegador = chrome.current_url
    numeroPokemonVersao = urlNavegador.split("/")[-1]
    extensaoImg = enderecoImage.split(".")[-1]
    nomeImagem = numeroPokemonVersao + "." + extensaoImg
    ondeSalvar = "TrabalhoIvan\\img\\" + nomeImagem

    wget.download(enderecoImage, ondeSalvar)

    print("Numero", elementNumero.text)
    print("Nome: ", elementNome.text)
    print("Altura: ", elementAltura.text)

    #adiciona os dados na planilha
    planilha.loc[contador] = [elementNumero.text, elementNome.text, elementAltura.text, nomeImagem]

    #seleciona o botão para o proximo pokemon
    btnNext = chrome.find_element(By.CSS_SELECTOR, ".pokemon-slider__wrapper--right > a")
    chrome.execute_script('arguments[0].click()', btnNext)

    #incremento para a parada do while
    contador = contador + 1

#salva a planilha em formato excel
planilha.to_excel('pokemon.xlsx', index=False)


#mantém a página aberta
input('Pressione enter para terminar')