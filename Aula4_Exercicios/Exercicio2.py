'''
Exercicio 2
-------------------------------------------------------------------
Crie um programa que recebe como entrada de dois numeros reais e um
operador matemático. De acordo com o operador matemático fornecido
o programa deve calcular e apresentar o resultado da operação.

Exemplo de entrada
1
2
+
Exemplo Saída

o Resultado da soma é 3
'''

print("Digite o primeiro número")
n1 = int(input())

print("Digite o segundo número")
n2 = int(input())

print("Digite o operador lógico( + , - , * , / )")
operador = input()

if  operador == "+":
    soma = n1 + n2
    print("Essa será a soma dos dois números:",soma)

elif operador == "-":
    subtração = n1 - n2
    print("Essa será a Subtração dos dois números:",subtração)

elif operador == "*":
    vezes = n1 * n2
    print("Essa será a multiplcação dos dois números:",vezes)

elif operador == "/":
    divisão = n1 / n2
    print("Essa será a divisão dos dois números:",divisão)