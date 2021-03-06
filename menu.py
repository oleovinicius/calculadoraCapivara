# -*- coding: utf-8 -*-
from constantes import constanteMenu
from logicaProposicional import LogicaProposicionalMenu
from matriz import matrizMenu
from somatoria import somatoriaMenu
from combinatoria import combinatoriaMenu
from funcao import funcaoMenu
from derivada import derivadaMenu
from integral import integralMenu
from calculadoraCapivara import *

def main():
    sair = False
    while sair == False:
        print("\nCalculadora Capivara")
        print("Menu principal:")
        sMenu = ['Somatoria', 'Constantes', 'Logica Proposicional', 'Matriz', 'Funcao',
                 'Combinatoria', 'Derivada Numerica', 'Integral Numerica','Modo Gráfico']

        for i, sMenu in enumerate(sMenu):
            print(' ', i + 1, '>>', sMenu)
        print("  0 > Sair")
        try:
            opc = int(input("DIGITE SUA OPCAO:"))

            if opc == 1:
                somatoriaMenu()
            elif opc == 2:
                constanteMenu()
            elif opc == 3:
                LogicaProposicionalMenu()
            elif opc == 4:
                matrizMenu()
            elif opc == 5:
                funcaoMenu()
            elif opc == 6:
                combinatoriaMenu()
            elif opc == 7:
                derivadaMenu()
            elif opc == 8:
                integralMenu()
            elif opc == 9:
                modoGrafico()

            elif opc == 0:
                print("Até a proxima ")
                sair = True
            else:
                print("Opção invalida!!!")
            pass
        except:
            print("\nENTRADA INVALIDA\n")




if __name__ == "__main__":
    main()
