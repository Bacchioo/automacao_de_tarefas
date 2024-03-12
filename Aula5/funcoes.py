'''
As funções são utilizadas para modularizar o código, ou, seja,
dividi-lo em partes menores, que podem ser reutilizadas.

Estrutura:

def nome_funcao(param1, param2):
    faz algo
    return valor

Exemplos!!!
'''
#Função 1
def calcularAreaTriangulo(base, altura):
    area = (base * altura) / 2
    return area

#Função 2
def login(usuario, senha):
    if usuario == 'admin' and senha == '123':
        return True
    else:
        return False
    
#Chamar a Função
    
#print(login("ivan", '123'))
#print("A área do triangulo é",calcularAreaTriangulo(100, 50))

