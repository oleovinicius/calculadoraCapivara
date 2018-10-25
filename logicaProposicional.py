
def LogicaProposicionalMenu():
    sair = False
    while sair == False :
        print("\nMenu Logica Proposicional")
        print("3.1 ¬ p")
        print("3.2 p ∧ q")
        print("3.3 p ∨ q")
        print("3.4 p ∨ q")
        print("3.5 p → q")
        print("3.6 p ↔ q")
        print("3.0 Menu principal")
        opc = int(input("DIGITE SUA OPÇÃO: "))

        if opc == 1:
            valorP = str(input("\nDigite TRUE ou FALSE para P:"))
            print("Valor da negação de P é: " + str(negacaoValor(valorP)))

        elif opc == 2:
            valorP = str(input("\nDigite TRUE ou FALSE para P:"))
            valorQ = str(input("\nDigite TRUE ou FALSE para Q:"))
            print("Valor da conjução é: " + str(conjucaoValores(valorP, valorQ)))

        elif opc == 3:
            valorP = str(input("\nDigite TRUE ou FALSE para P:"))
            valorQ = str(input("\nDigite TRUE ou FALSE para Q:"))
            print("Valor da disjunção é: " + str(disjuncaoValores(valorP, valorQ)))

        elif opc == 4:
            valorP = str(input("\nDigite TRUE ou FALSE para P:"))
            valorQ = str(input("\nDigite TRUE ou FALSE para Q:"))
            print("Valor da disjunção exclusiva é: " + str(disjuncaoExValores(valorP, valorQ)))

        elif opc == 5:
            valorP = str(input("\nDigite TRUE ou FALSE para P:"))
            valorQ = str(input("\nDigite TRUE ou FALSE para Q:"))
            print("Valor da condicional é: " + str(condicionalValores(valorP, valorQ)))

        elif opc == 6:
            valorP = str(input("\nDigite TRUE ou FALSE para P:"))
            valorQ = str(input("\nDigite TRUE ou FALSE para Q:"))
            print("Valor da equivalencia é: " + str(equivalenciaValores(valorP, valorQ)))


        elif opc == 0:
            sair = True

        else:
            print("\nOPÇÃO INVALIDA!!!\n")

def verificaValores(n):
    if n == "True" or n == "true" or n == "TRUE":
        return True
    elif n == "False" or n == "false" or n == "FALSE":
        return False
    else:
        print(n)
        return print ("\nPARAMETRO INVALIDO!!\n")

def negacaoValor(p):
    p = verificaValores(p)
    return not(p)

def conjucaoValores(P,Q):
    p = verificaValores(P)
    q = verificaValores(Q)
    return bool(p and q)

def disjuncaoValores(P,Q):
    p = verificaValores(P)
    q = verificaValores(Q)
    return bool(p or q)

def condicionalValores(P,Q):
    p = verificaValores(P)
    q = verificaValores(Q)
    return (not(p) or q)

def equivalenciaValores(P,Q):
    casoUm = condicionalValores(P, Q)
    casoDois = condicionalValores(Q, P)
    return (casoUm and casoDois)

def disjuncaoExValores(P,Q):
    res = equivalenciaValores(P,Q)
    return not(res)
