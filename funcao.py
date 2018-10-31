import numpy as np
from constantes import constanteEuler
from decimal import Decimal, getcontext

getcontext().prec=1000

def funcaoMenu():
    sair = False
    while sair== False:
        print("\nMenu de combinatoria")
        cMenu = ['f(x)= k', 'f(x)= x^k',
                 'f(x)= k^x', 'f(x)= logk(x)',
                 'f(x)= sen(x)', 'f(x)= cos(x)',
                 'f(x)= tan(x)', 'f(x)= √x',
                 'f(x)= 1/x', 'f(x)= e^x',
                 'f(x)= ln(x)']
        for i, cMenu in enumerate(cMenu):
            print('5.', i + 1, ' - ', cMenu, sep='')
        print("5.0 menu principal")

        try:
            opc = int(input("DIGITE SUA OPÇÃO:"))
            if opc == 1:
                try:
                    aux = float(input("\nDigite um valor para K:"))
                    print("Valor da constante:", constante(aux))
                except:
                    print("Parametrização Errada!!!")
            if opc == 2:
                try:
                    x = float(input("\nDigite um valor para x:"))
                    k = float(input("\nDigite um valor para K:"))
                    print("Valor de",x,"elevado a",k,':' ,elevado(x, k))
                except:
                    print("Parametrização Errada!!!")
            if opc == 3:
                try:
                    x = float(input("\nDigite um valor para x:"))
                    k = float(input("\nDigite um valor para K:"))
                    print("Valor de", k, "elevado a", x, ':', elevado(k, x))
                except:
                    print("Parametrização Errada!!!")
            if opc == 4:
                try:
                    x = float(input("\nDigite um valor para x:"))
                    k = float(input("\nDigite um valor para K:"))
                    print("Valor do logaritimo de", x, "na base", k, ':', log(x,k))
                except:
                    print("Parametrização Errada!!!")
            if opc == 5:
                try:
                    x = float(input("\nDigite um valor para x:"))
                    print("Valor do seno de", x,':', seno(x))
                except:
                    print("Parametrização Errada!!!")
            if opc == 6:
                try:
                    x = float(input("\nDigite um valor para x:"))
                    print("Valor do cosseno de", x,':', cos(x))
                except:
                    print("Parametrização Errada!!!")
            if opc == 7:
                try:
                    x = float(input("\nDigite um valor para x:"))
                    print("Valor da tangente de", x,':', tag(x))
                except:
                    print("Parametrização Errada!!!")
            if opc == 8:
                try:
                    x = float(input("\nDigite um valor para x:"))
                    print("Valor da raiz de", x,':', raiz(x))
                except:
                    print("Parametrização Errada!!!")
            if opc == 9:
                try:
                    x = float(input("\nDigite um valor para x:"))
                    print("Valor do 1 dividido por ", x,':', umSobre(x))
                except:
                    print("Parametrização Errada!!!")
            if opc == 10:
                try:
                    x = float(input("\nDigite um valor para x:"))
                    print("Valor de euler elevado a", x,':', eulerElevado(x))
                except:
                    print("Parametrização Errada!!!")
            if opc == 11:
                try:
                    x = float(input("\nDigite um valor para x:"))
                    print("Valor de ln de", x,':', logaritimoNatural(x))
                except:
                    print("Parametrização Errada!!!")
            elif opc == 0:
                sair = True
            pass
        except:
            print("Opção invalida!!")
            pass

def constante(n):
    return n

def elevado(k,x):
    res = k**x
    return res

def log(x,k):
    res = np.log10(x)/np.log10(k)
    return res

def seno(n):
    res = np.sin(n)
    return res

def cos(n):
    res = np.cos(n)
    return res

def tag(n):
    res = np.tan(n)
    return res

def raiz(n):
    res = np.sqrt(n)
    return res

def umSobre(n):
    res = 1/n
    return res

def eulerElevado(n):
    res = constanteEuler(999999)**n
    return res

def logaritimoNatural(n):
    res = np.log(n)
    return res
