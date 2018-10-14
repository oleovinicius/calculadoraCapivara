import string
from somatoria import somatoriaMenu

def main():
    print("Calculadora Capivara")
    print("Menu principal:")
    sMenu = ['Somatoria', 'Constantes', 'Logica Proposicional', 'Matriz', 'Funcao',
             'Combinatoria', 'Derivada Numerica', 'Integral Numerica']

    for i, sMenu in enumerate(sMenu):
        print(' ', i + 1, '-', sMenu)
    print("  0-Sair")
    opc = int(input("DIGITE SUA OPCAO:"))


    if  opc == 1:
        somatoriaMenu()
    elif opc == 0:print("Até a proxima ")
    else:print("Opção invalida!!!")

if __name__ == "__main__":
    main()
