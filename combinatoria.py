import scipy
from math import factorial
def combinatoriaMenu():
    sair = False
    while sair== False:
        print("\nMenu de combinatoria")
        cMenu = ['Permutação Simples: P(n)', 'Permutação com Repetição: PR(n,n1,n2,...,nk)',
                 'Arranjo Simples: A(n,p)', 'Arranjo com Repetição: AR(n,p)',
                 'Combinação Simples: C(n,p)', 'Combinação com Repetição: CR(n,p)']
        for i, cMenu in enumerate(cMenu):
            print(' 5.',i + 1,'-', cMenu)
        print("5.0 menu principal")
        try:
            opc = int(input("DIGITE SUA OPÇÃO:"))

            if opc == 1:
                try:
                    n = int(input("Digite um valor para n:"))
                    print("Permutação simples de", str(n), "é:",str(permSimples(n)))
                except:
                    print("Parametrização errada!")
            if opc == 2:
                try:
                    n = int(input("Digite um valor para n:"))
                    p = int(input("Digite um valor para p(constante):"))
                    print("Resultado da Permutação com repetição de", str(n), "é:", str(permRepeticao(n,p)))
                except:
                    print("Parametrização errada!")
            if opc == 3:
                try:
                    n = int(input("Digite um valor para n:"))
                    p = int(input("Digite um valor para p(Qtd. de elementos por arranjo):"))
                    print("Resultado do arranjo simples de", str(n), "e", str(p), "é:", str(arranjoSimples(n,p)))
                except:
                    print("Parametrização errada!")
            if opc == 4:
                try:
                    n = int(input("Digite um valor para n:"))
                    p = int(input("Digite um valor para p(Qtd. de repetições):"))
                    print("Resultado do arranjo simples com repetição de", str(n), "e", str(p), "é:", str(arranjoRepetição(n,p)))
                except:
                    print("Parametrização errada!")
            if opc == 5:
                try:
                    n = int(input("Digite um valor para n:"))
                    p = int(input("Digite um valor para p(Qtd. de elementros subconjuntos):"))
                    print("Resultado da combinação simples de", str(n), "e", str(p), "é:", str(combSimples(n, p)))
                except:
                    print("Parametrização errada!")
            if opc == 6:
                try:
                    n = int(input("Digite um valor para n:"))
                    p = int(input("Digite um valor para p(Qtd. de elementros subconjuntos):"))
                    print("Resultado da combinação com repetição de", str(n), "e", str(p), "é:", str(combSimples(n, p)))
                except:
                    print("Parametrização errada!")


            elif opc == 0:
                sair = True
            pass
        except:
            print("\nENTRADA INVALIDA\n")

def permSimples(n):
    result = factorial(n)
    return result

def permRepeticao(n,p):
    result =(factorial(n)//p)
    return result
def arranjoSimples(n,p):
    result = (factorial(n)/ factorial(n-p))
    return result
def arranjoRepetição(n,p):
    result = (n**p)
    return result
def combSimples(n,p):
    result = factorial(n)/(factorial(p)*(factorial(n-p)))
    return result
def combRepet(n,p):
    result = factorial(n+p-1)/(factorial(p)*factorial(n-1))
    return result