'''
Exercicio 1
-------------------------------------------------------------------
Crie um programa que recebe como entrada dois números reais.
O programa deve imprimir as quatros operações matematicas entre
os dois números (soma,subtração,divisão e multiplicação).
'''

n1 = int(input("Digite o primeiro número\n"))
n2 = int(input("Digite o segundo número\n"))

Soma = n1+n2
Vezes = n1*n2
Divisão = n1/n2
Subtração = n1-n2
print("Essa será a soma dos dois números:",Soma)
print("Essa será a subtração dos dois números:",Subtração)
print("Essa será a multiplicação dos dois números:",Vezes)
print("Essa será a divisão dos dois números:",Divisão)