import numpy as np

def derivadaMenu():
    sair = False
    while sair == False:
        print("\nMenu de derivada")
        dMenu = ['f(x)= K','f(x)= K^X','f(x)= X^K',
        'f(x)= logk(x)','f(x)= sen(x) ','f(x)= cos(x)',
        'f(x)= tan(x)','f(x)= √x','f(x)= 1/x',
        'f(x)= e^x','f(x)= ln(x)',]

        for i, dMenu in enumerate(dMenu):
            print('7.',i + 1,'-', dMenu)
        print("7.0 menu principal")
        try:
            opc = int(input("DIGITE SUA OPÇÃO:"))

            if opc == 1:
                try:
                    K = float(input("Digite o valor para K:"))
                    print(K)
                    print("Derivada de", K, "é:", derivadaConstantes(K))
                except:
                    print("Parametrização errada!!")
            elif opc == 2:
                try:
                    K = float(input("Digite o valor para K:"))
                    X = float(input("Digite o valor para X:"))
                    print("Derivada de", K,"elevado",X,"é:", derivadaConstanteElevado(X,K))
                except:
                    print("Parametrização errada!!")
            elif opc == 3:
                try:
                    K = float(input("Digite o valor para K:"))
                    X = float(input("Digite o valor para X:"))
                    print("Derivada de", X,"elevado",K,"é:", derivadaElevadoConstante(X,K))
                except:
                    print("Parametrização errada!!")
            elif opc == 4:
                try:
                    K = float(input("Digite o valor para K:"))
                    X = float(input("Digite o valor para X:"))
                    print("Derivada de log de", X,'na base',K,"é:", derivadaLog(K,X))
                except:
                    print("Parametrização errada!!")
            elif opc == 5:
                try:
                    X = float(input("Digite o valor para X:"))
                    XConv = converteGrausRadianos(X)
                    print("Derivada de seno de", X,"é:", derivadaSen(XConv))
                except:
                    print("Parametrização errada!!")
            elif opc == 6:
                try:
                    X = float(input("Digite o valor para X:"))
                    XConv = converteGrausRadianos(X)
                    print("Derivada de cosseno de", X,"é:", derivadaCos(XConv))
                except:
                    print("Parametrização errada!!")
            elif opc == 7:
                try:
                    X = float(input("Digite o valor para X:"))
                    XConv = converteGrausRadianos(X)
                    print("Derivada de tangente de", X,"é:", derivadaTan(XConv))
                except:
                    print("Parametrização errada!!")
            elif opc == 8:
                try:
                    X = float(input("Digite o valor para X:"))
                    print("Derivada de raiz de", X,"é:", derivadaRaiz(X))
                except:
                    print("Parametrização errada!!")
            elif opc == 9:
                try:
                    X = float(input("Digite o valor para X:"))
                    print("Derivada de 1/x de", X,"é:", derivadaUmSobre(X))
                except:
                    print("Parametrização errada!!")
            elif opc == 10:
                try:
                    X = float(input("Digite o valor para X:"))
                    print("Derivada de euler em", X,"é:", derivadaEuler(X))
                except:
                    print("Parametrização errada!!")
            elif opc == 11:
                try:
                    X = float(input("Digite o valor para X:"))
                    print("Derivada de ln de", X,"é:", derivadaLogaritimoNatural(X))
                except:
                    print("Parametrização errada!!")

            elif opc == 0:
                sair = True

        except:
            print("Opção invalida!!!")

        pass

def converteGrausRadianos(x):
    res = (x*np.pi)/180
    return res

def derivadaConstantes(n):
    return 0

def derivadaElevadoConstante(x,k):
    res = k*(x**(k-1))
    return res

def derivadaConstanteElevado(x,k):
    res = (k**x)*np.log(k)
    return res

def derivadaLog(k,x):
    res = 1/(x*np.log(k))
    return res

def derivadaSen(x):
    res = np.cos(x)
    return res

def derivadaCos(x):
    res = -1*(np.sin(x))
    return res

def derivadaTan(x):
    res = (1/np.cos(x))**2
    return res

def derivadaRaiz(x):
    res = x**0.5
    return res

def derivadaUmSobre(x):
    res = -1/(x**2)
    return res

def derivadaEuler(x):
    return 0

def derivadaLogaritimoNatural(x):
    if x != 0:
        res = 1/x
    else:
        res = "X deve ser diferente de 0"
    return res
