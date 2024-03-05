print('Digite sua idade: ') 
idade = int(input())

if idade <= 12:
    print("Você ainda esta Amadurecendo")
elif idade < 18:
    print("Você é comível agora")
elif idade < 60:
    print("Pague as Contas")
else:
    print("Aposentadoria Liberada, Aproveite")

print("Sua idade no ano que vem será ", idade + 1)