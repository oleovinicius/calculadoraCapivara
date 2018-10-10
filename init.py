import string


def menu():
    sMenu = ['Somatoria', 'Constantes', 'Logica Proposicional', 'Matriz', 'Funcao',
             'Combinatoria', 'Derivada Numerica', 'Integral Numerica']

    for i, sMenu in enumerate(sMenu):
        print(' ', i + 1, '-', sMenu)
    print("  0-Sair")
    opc = input("DIGITE SUA OPCAO:")
    switch


def main():
    menu()


print("Calculadora Capivara")
main()
