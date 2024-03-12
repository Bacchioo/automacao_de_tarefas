from funcoes import login

while True:
    user = input('Digite o nome de usuário: ')
    pwd = input('Digite o senha de usuário: ')
    if login(user, pwd):
        print('Logado com sucesso!')
        break
    else:
        print('Tente novamente!')
        