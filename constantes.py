from math import factorial
from decimal import Decimal, getcontext

getcontext().prec=100

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
            k = int(input("Digite o valor de K:"))
            print("Valor de PI:"+ str(ConstPI(k)))
            #constantePi(passos, k)

        elif opc == 2:
            print("\nPara calcular o valor Euler(e) utiliza-se:")
            print("e (1+(1/k))^k")
            k = float(input("Digite a constante K:"))
            print("Resultado Euler:" + str(constanteEuler(k)))
                    
        elif opc == 0:
            sair = True
        else:print("OPÇÃO INVALIDA !!!")
        pass

# def constantePi(passos, k):
#     valorPi =3.00
#     for k in range(k, passos):
#         j = 4*k
#         valorPi= float(valorPi + (8/((j+1)*(j+3))))
#         pass
#     return print("Valor de PI:" + str(valorPi))

def constanteEuler(constante):
    euler = 0.00
    euler = (1+(1/constante))**constante
    return euler

def ConstPI(n):
	t= Decimal(0)
	pi = Decimal(0)
	deno= Decimal(0)
	k = 0
	for k in range(n):
		t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
		deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
		pi += Decimal(t)/Decimal(deno)
	#pi = pi * Decimal(12)/Decimal(640320**(1.5))
	pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
	pi = 1/pi
	return pi
