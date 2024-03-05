#while
'''
Repete enquanto uma condição for verdadeira
'''

print("\nExemplo 1:")
i = 0
while i < 5:
    print(i, "CARAI TO LOMBRADO")
    i = i + 1

print("\nExemplo 2:")
nomes = []
while True:
    nome = input("Digite um nome: ")
    nomes.append(nome)
    if (nome == 'fim'):
        print(nomes)
        break