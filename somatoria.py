def somatoriaMenu():
    # ALT + ?? == Σ
    sair=False
    while sair == False:
        print("\nMenu de somatoria")
        print("1.1- Σ N = A^k ")
        print("1.2- Σ N = (A^k)^M")
        print("1.3- Σ N = (A^M)^k ")
        print("1.0- menu principal")
        print("OBS: k é o numero inicial de passos, o valor A será uma constante,"
        " N será o numero de passos e M outra constante")
        opc =int(input("DIGITE SUA OPÇÃO:"))

        if opc == 1:
            passos =int(input("\nDigite o valor de N:"))+1
            constante =float(input("Digite o valor de A:"))
            inicio =int(input("Digite o valor de k:"))
            somatoriaUm(passos, constante, inicio)
            print("Resultado Somatoria: " + str(somatoriaUm(passos, constante, inicio)))
        elif opc == 2:
            passos =int(input("\nDigite o valor de N:"))+1
            constante =float(input("Digite o valor de A:"))
            extra =int(input("Digite o valor do M:"))
            inicio =int(input("Digite o valor de k:"))
            somatoriaDois(passos, constante, extra, inicio)
            print("Resultado Somatoria: " + str(somatoriaDois(passos, constante, extra, inicio)))
        elif opc == 3:
            passos =int(input("\nDigite o valor de N:"))+1
            constante =float(input("Digite o valor de A:"))
            extra =int(input("Digite o valor do M:"))
            inicio =int(input("Digite o valor de k:"))
            somatoriaTres(passos, constante, extra, inicio)
            print("Resultado Somatoria: " + str(somatoriaTres(passos, constante, extra, inicio)))
        elif opc == 0:
            sair = True
        else:print("OPÇÃO INVALIDA !!!")
        pass

def somatoriaUm(passos, constantes, inicio):
    somatoriaResultado=0
    for inicio in range(inicio,passos):
        somatoriaResultado=somatoriaResultado+(constantes**inicio)
        # print("Passo Atual:" + str(inicio))
    return somatoriaResultado

def somatoriaDois(passos,constantes,extra, inicio):
    somatoriaResultado=0
    for inicio in range(inicio,passos):
        somatoriaResultado=somatoriaResultado+((constantes**inicio)**extra)
        #print("Passo Atual:" + str(k))
    return somatoriaResultado


def somatoriaTres(passos,constantes,extra, inicio):
    somatoriaResultado=0
    for inicio in range(inicio,passos):
        somatoriaResultado=(somatoriaResultado+((constantes**extra)**inicio))
        # print("Passo Atual:" + str(inicio))
    return somatoriaResultado
