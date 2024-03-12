'''
Para utilizarmos  as funções criadas em outros
arquivos de código fonte devemos importa-las. para
isso utilizamos o comando import ou from import

Exemplo1: Importar todas as funções do arquivo funções
'''
import funcoes as Funcoes

base = float(input('Digite a base do triangulo: '))
altura = float(input('Digite a altura do triangulo: '))

area = Funcoes.calcularAreaTriangulo(base,altura)
print('A area do triangulo é: ',area)