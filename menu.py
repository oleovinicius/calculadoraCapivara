# -*- coding: utf-8 -*-
import string
from somatoria import *
from constantes import *

def main():
    sair = False
    while sair == False:
        print("\nCalculadora Capivara")
        print("Menu principal:")
        sMenu = ['Somatoria', 'Constantes', 'Logica Proposicional', 'Matriz', 'Funcao',
                 'Combinatoria', 'Derivada Numerica', 'Integral Numerica']

        for i, sMenu in enumerate(sMenu):
            print(' ', i + 1, '-', sMenu)
        print("  0 - Sair")
        opc = int(input("DIGITE SUA OPCAO:"))


        if  opc == 1:
            somatoriaMenu()
        elif opc == 2:
            constanteMenu()
        elif opc == 0:
            print("Até a proxima ")
            sair=True
        else:print("Opção invalida!!!")
        pass

if __name__ == "__main__":
    main()
