def menu():
    print("1. Criptografar\n2. Descriptografar\n3. Sair")

def menu2():
    print("1. Modo 1\n2. Modo 2")

def criptografar():
    global palavra
    palavra=input("O que quer criptografar: ")

def descriptografar():
    global palavra
    palavra=input("O que quer descriptografar: ")

def exit():
    print("1. Sair\n2. Cancelar")

opcao=1
while opcao!=3:
    menu()
    opcao=int(input("Digite sua opção: "))

    if opcao==1:
        criptografar()

        menu2()
        modo=int(input("Como deseja criptografar: "))

        if modo==1:
            mensagem=""
            for i in palavra:
             mensagem = mensagem + chr(ord(i)-30)
            print(mensagem[::-1])

        elif modo==2:
          mensagem=""
          for i in palavra:
              mensagem = mensagem + chr(ord(i)-15)
          print(mensagem[::-1])
    
        else:
         print("Modo inválido")

    elif opcao==2:
        descriptografar()

        menu2()
        modo=int(input("Como deseja descriptografar: "))

        if modo==1:
            mensagem=""
            for i in palavra:
                mensagem = mensagem + chr(ord(i)+30)
            print(mensagem[::-1])

        elif modo==2:
            mensagem=""
            for i in palavra:
                mensagem = mensagem + chr(ord(i)+15)
            print(mensagem[::-1])

        else:
            print("Modo inválido")
    elif opcao==3:
        exit()
        opcao=int(input("Deseja sair? "))
        if opcao==1:
            print("Exit")
            break

    else:
        print("Opção inválida")
        break