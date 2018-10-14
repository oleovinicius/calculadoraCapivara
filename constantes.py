def constanteMenu():
    sair = False
    while sair == False:
        print("\nMenu de constantes")
        print("2.1 Valor de π")
        print("2.2 Valor de e")
        print("2.0 menu principal")
        opc =int(input("DIGITE SUA OPÇÃO:"))

        if opc == 1:
            print("\nPara calcular o valor de PI(𝜋) utiliza-se:")
            print(" n")
            print(" Σ = 8/(((4*k)+1)*((4*k)+3))")
            print(" k=0")
            passos = int(input("Digite o valor de N:"))+1
            k = int(input("Digite o valor de K:"))
            constantePi(passos, k)

        elif opc == 2:
            print("\nPara calcular o valor Euler(e) utiliza-se:")
            print("e (1+(1/k))^k")
            k = float(input("Digite a constante K:"))
            constanteEuler(k)
        elif opc == 0:
            sair = True
        else:print("OPÇÃO INVALIDA !!!")
        pass

def constantePi(passos, k):
    valorPi =3.00
    for k in range(k, passos):
        j = 4*k
        valorPi= float(valorPi + (8/((j+1)*(j+3))))
        pass
    return print("Valor de PI:" + str(valorPi))

def constanteEuler(constante):
    euler = 0.00
    euler = (1+(1/constante))**constante
    return print("Resultado Euler:" + str(euler))
