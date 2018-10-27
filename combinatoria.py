

def combinatoriaMenu():
    sair = False
    while sair== False:
        print("\nMenu de combinatoria")
        cMenu = ['Permutação Simples: P(n)', 'Permutação com Repetição: PR(n,n1,n2,...,nk)',
                 'Arranjo Simples: A(n,p)', 'Arranjo com Repetição: AR(n,p)',
                 'Combinação Simples: C(n,p)', 'Combinação com Repetição: CR(n,p)']
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