import sys
usuário = []
senha = []
def login():
    print('='*20,'Login','='*20)
    print("\033[37mentrar em conta existente\033[m")
    print("\033[36mcriar nova conta\033[m")
    alfa = input("")
    if alfa == 'entrar em conta existente' or alfa == '1':
        A = input("Usuário: ")
        B = input("Senha: ")
        if A in usuário and B in senha:
            print("\033[32mUsuário Cadastrado com sucesso!\033[m")
            sys.exit()
        else:
            print("\033[31mUsuário não encontrado. Tente novamente\033[m")
    if alfa == 'criar nova conta' or alfa == '2':
        C = input("Inserir nome de usuário: ")
        usuário.append(C)
        D = input("Inserir senha: ")
        senha.append(D)
        E = input("Repetir senha: ")
        while E != D:
            print("\033[31mErro, as senhas não estão batendo\033[m")
            E = input("Repetir senha: ")
            if E == D:
                print("\033[32mNovo usuário cadastrado!\033[m")

    return login()
login()