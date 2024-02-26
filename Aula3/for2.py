#Repetição simples: 10 vezes - de 0 a 9
print('\nExemplo 1')
for i in range(0,10):
    print(i, "CARAI")

#Repetição com passo <> 1: repete5 vezes de 2 em 2
print('\nExemplo 2')
for i in range(0, 10, 2):
    print(i, "ALEK")

#Repetição decreste
print('\nExemplo 3')
for i in range(10, 0, -1):
    print(i, "T0")

#Repetição com listas
print('\nExemplo 4.1 - imprime o nome da lista')
alunos = ["julia", "kayky", "Inessa", "Adriano"]
for nome in alunos:
    print(nome)

print('\nExemplo 4.2 - imprime posição e nome da lista')
for index, nome in enumerate(alunos):
    print(index,nome)

