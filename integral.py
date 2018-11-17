import numpy as np

def integralMenu():
    sair = False
    while sair == False:
        print("\nMenu de integral")
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
                    a = int(input("Digite o valor de A:"))
                    b = int(input("Digite o valor de B:"))
                    print(K)
                    print("Integral de", K, "é:", integralConstantes(K,b,a))
                except:
                    print("Parametrização errada!!")
            elif opc == 2:
                try:
                    K = float(input("Digite o valor para K:"))
                    a = int(input("Digite o valor de A:"))
                    b = int(input("Digite o valor de B:"))
                    print("Integral de", K,"elevado",X,"é:", integralConstanteElevado(K,b,a))
                except:
                    print("Parametrização errada!!")
            elif opc == 3:
                try:
                    K = float(input("Digite o valor para K:"))
                    X = float(input("Digite o valor para X:"))
                    a = int(input("Digite o valor de A:"))
                    b = int(input("Digite o valor de B:"))
                    print("Integral de", X,"elevado",K,"é:", integralElevadoConstante(X,K,b,a))
                except:
                    print("Parametrização errada!!")
            elif opc == 4:
                try:
                    K = float(input("Digite o valor para K:"))
                    X = float(input("Digite o valor para X:"))
                    a = int(input("Digite o valor de A:"))
                    b = int(input("Digite o valor de B:"))
                    print("Integral de log de", X,'na base',K,"é:", integralLog(K,X,b,a))
                except:
                    print("Parametrização errada!!")
            elif opc == 5:
                try:
                    X = float(input("Digite o valor para X:"))
                    a = int(input("Digite o valor de A:"))
                    b = int(input("Digite o valor de B:"))
                    XConv = converteGrausRadianos(X)
                    print("Integral de seno de", X,"é:", integralSen(XConv,b,a))
                except:
                    print("Parametrização errada!!")
            elif opc == 6:
                try:
                    X = float(input("Digite o valor para X:"))
                    a = int(input("Digite o valor de A:"))
                    b = int(input("Digite o valor de B:"))
                    XConv = converteGrausRadianos(X)
                    print("Integral de cosseno de", X,"é:", integralCos(XConv,b,a))
                except:
                    print("Parametrização errada!!")
            elif opc == 7:
                try:
                    X = float(input("Digite o valor para X:"))
                    a = int(input("Digite o valor de A:"))
                    b = int(input("Digite o valor de B:"))
                    XConv = converteGrausRadianos(X)
                    print("Integral de tangente de", X,"é:", integralTan(XConv,b,a))
                except:
                    print("Parametrização errada!!")
            elif opc == 8:
                try:
                    X = float(input("Digite o valor para X:"))
                    a = int(input("Digite o valor de A:"))
                    b = int(input("Digite o valor de B:"))
                    print("Integral de raiz de", X,"é:", integralRaiz(X,b,a))
                except:
                    print("Parametrização errada!!")
            elif opc == 9:
                try:
                    X = float(input("Digite o valor para X:"))
                    a = int(input("Digite o valor de A:"))
                    b = int(input("Digite o valor de B:"))
                    print("Integral de 1/x de", X,"é:", integralUmSobre(X,b,a))
                except:
                    print("Parametrização errada!!")
            elif opc == 10:
                try:
                    X = float(input("Digite o valor para X:"))
                    a = int(input("Digite o valor de A:"))
                    b = int(input("Digite o valor de B:"))
                    print("Integral de euler em", X,"é:", integralEuler(X,b,a))
                except:
                    print("Parametrização errada!!")
            elif opc == 11:
                try:
                    X = float(input("Digite o valor para X:"))
                    a = int(input("Digite o valor de A:"))
                    b = int(input("Digite o valor de B:"))
                    print("Integral de ln de", X,"é:", integralLogaritimoNatural(X,b,a))
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

def integralConstantes(n,b,a):
    res = (n*b) - (n*a)
    return res

def integralElevadoConstante(k,b,a):
    res = ((b**(k+1))/(k+1)) - ((a**(k+1))/(k+1))
    return res

def integralConstanteElevado(k,b,a):
    res = (k**b)/(np.log(b)) - (k**a)/(np.log(a))
    return res

def integralLog(k,b,a):
    res = ((b*np.log(b)-b)/np.log(k))-((a*np.log(a)-a)/np.log(k))
    return res

def integralSen(b,a):
    res = (-1*np.cos(b))-(-1*np.cos(a))
    return res

def integralCos(b,a):
    res = (np.sin(b))-(np.sin(a))
    return res

def integralTan(x,b,a):
    res = (1/np.cos(x))**20
    return res

def integralRaiz(x,b,a):
    res = x**0.5
    return res

def integralUmSobre(x,b,a):
    res = np.log(b) - np.log(a)
    return res

def integralEuler(x,b,a):
    return 0

def integralLogaritimoNatural(x,b,a):
    if x != 0:
        res = 1/x
    else:
        res = "X deve ser diferente de 0"
    return res
