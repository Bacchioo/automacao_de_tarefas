'''
Exercicio 3
-------------------------------------------------------------------
Crie um programa que execute o programa do exercicio 2. Após a 
apresentação do resultado o programa deve perguntar se o usuário
deseja continuar a calcular, se a resposta for S (Sim) o programa 
deve continuar se a resposta for N (Não) o programa deve terminar.
'''
res = True
while res == True:
    print("Digite o primeiro número")
    n1 = int(input())

    print("Digite o segundo número")
    n2 = int(input())

    print("Digite o operador lógico( + , - , * , / )")
    operador = input()

    if  operador == "+":
        soma = n1 + n2
        print("Essa será a soma dos dois números:",soma)
        res = input("Digite S(Sim) para continuar ou N(Não) para parar o código.")
        if res == "N":
            break
        elif res == "S":
            res = True

    if operador == "-":
        subtração = n1 - n2
        print("Essa será a Subtração dos dois números:",subtração)
        res = input("Digite S(Sim) para continuar ou N(Não) para parar o código.")
        if res == "N":
            break
        elif res == "S":
            res = True

    if operador == "*":
        vezes = n1 * n2
        print("Essa será a multiplcação dos dois números:",vezes)
        res = input("Digite S(Sim) para continuar ou N(Não) para parar o código.")
        if res == "N":
            break
        elif res == "S":
            res = True

    if operador == "/":
        divisão = n1 / n2
        print("Essa será a divisão dos dois números:",divisão)
        res = input("Digite S(Sim) para continuar ou N(Não) para parar o código.")
        if res == "N":
            break
        elif res == "S":
            res = True
            