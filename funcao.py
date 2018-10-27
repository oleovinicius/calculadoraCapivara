def funcaoMenu():
    sair = False
    while sair== False:
        print("\nMenu de combinatoria")
        cMenu = ['f(x)= k', 'f(x)= x^k',
                 'f(x)= k^x', 'f(x)=',
                 'f(x)=', 'f(x)=']
        for i, cMenu in enumerate(cMenu):
            print('5.',i + 1,'-', cMenu)
        print("5.0 menu principal")
        opc = int(input("DIGITE SUA OPÇÃO:"))

        if opc == 1:
            print("nd ate aqui")
        elif opc == 0:
            sair = True
        else:print("OPÇÃO INVALIDA !!!")

        pass