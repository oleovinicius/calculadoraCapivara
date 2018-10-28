import numpy as np


def matrizMenu():
    sair = False
    while sair == False:
        print("\nMenu de matriz")
        print("4.1 Soma")
        print("4.2 Subtração")
        print("4.3 Produto")
        print("4.4 Determinante")
        print("4.0 Menu principal")
        try:
            opc = int(input("DIGITE SUA OPÇÃO:"))

            if opc == 1:
                try:
                    mlinhas = int(input("Digite o numero de linhas:"))
                    ncolunas = int(input("Digite o numero de colunas:"))
                    aux = somaMatriz(mlinhas, ncolunas)
                    print("Soma das matrizes:")
                    print(aux)
                except:
                    print("Parametrização errada")
            if opc == 2:
                try:
                    mlinhas = int(input("Digite o numero de linhas:"))
                    ncolunas = int(input("Digite o numero de colunas:"))
                    aux = subMatriz(mlinhas, ncolunas)
                    print("Subtração das matrizes:")
                    print(aux)
                except:
                    print("Parametrização errada")
            if opc == 3:
                try:
                    mlinhas = int(input("Digite o numero de linhas:"))
                    ncolunas = int(input("Digite o numero de colunas:"))
                    # aux =
                    print("Produto das matrizes:\n", str(prodMatriz(mlinhas, ncolunas)))
                    # print(aux)
                except:
                    print("Parametrização errada")
            if opc == 4:
                try:
                    mlinhas = int(input("Digite o numero de linhas:"))
                    ncolunas = int(input("Digite o numero de colunas:"))
                    print("Determinante entre duas matrizes:\n", str(determMatriz(mlinhas,ncolunas)))
                except:
                    print("Parametrização errada")


            elif opc == 0:
                sair = True

            pass
        except:
            print("\nENTRADA INVALIDA\n")


def somaMatriz(m, n):
    matrizA = np.zeros(shape=(m, n))
    matrizB = np.zeros(shape=(m, n))
    matrizResultado = np.zeros(shape=(m, n))
    for l in range(0, m):
        for c in range(0, n):
            matrizA[l][c] = int(input(f"Digite o valor para [{l}, {c}]:"))

    print("matrizA:")
    print(matrizA)
    for l in range(0, m):
        for c in range(0, n):
            matrizB[l][c] = int(input(f"Digite o valor para [{l}, {c}]:"))

    print("matrizB:")
    print(matrizB)
    # Somando Matrizes
    for l in range(0, m):
        for c in range(0, n):
            matrizResultado[l][c] = matrizA[l][c] + matrizB[l][c]
            # matrizB[l][c] = int(input(f"Digite o valor para [{l}, {c}]:"))
    return matrizResultado



def subMatriz(m, n):
    matrizA = np.zeros(shape=(m, n))
    matrizB = np.zeros(shape=(m, n))
    matrizResultado = np.zeros(shape=(m, n))
    for l in range(0, m):
        for c in range(0, n):
            matrizA[l][c] = int(input(f"Digite o valor para [{l}, {c}]:"))

    print("matrizA:")
    print(matrizA)
    for l in range(0, m):
        for c in range(0, n):
            matrizB[l][c] = int(input(f"Digite o valor para [{l}, {c}]:"))

    print("matrizB:")
    print(matrizB)
    # Subtraindo Matrizes
    for l in range(0, m):
        for c in range(0, n):
            matrizResultado[l][c] = matrizA[l][c] - matrizB[l][c]
            # matrizB[l][c] = int(input(f"Digite o valor para [{l}, {c}]:"))
    return matrizResultado

def prodMatriz(m, n):
    matrizA = np.zeros(shape=(m, n))
    matrizB = np.zeros(shape=(m, n))
    matrizResultado = np.zeros(shape=(m, n))
    for l in range(0, m):
        for c in range(0, n):
            matrizA[l][c] = int(input(f"Digite o valor para [{l}, {c}]:"))

    print("matrizA:")
    print(matrizA)
    for l in range(0, m):
        for c in range(0, n):
            matrizB[l][c] = int(input(f"Digite o valor para [{l}, {c}]:"))
    print("matrizB:")
    print(matrizB)
    # Fazendo o produto das Matrizes
    matrizResultado = matrizA.dot(matrizB)
    return matrizResultado

def determMatriz(m, n):
    matrizA = np.zeros(shape=(m, n))
    matrizB = np.zeros(shape=(m, n))
    matrizResultado = np.zeros(shape=(m, n))
    for l in range(0, m):
        for c in range(0, n):
            matrizA[l][c] = int(input(f"Digite o valor para [{l}, {c}]:"))

    print("matrizA:")
    print(matrizA)
    for l in range(0, m):
        for c in range(0, n):
            matrizB[l][c] = int(input(f"Digite o valor para [{l}, {c}]:"))
    print("matrizB:")
    print(matrizB)
    # Fazendo a determinante das Matrizes
    matrizResultado = np.matmul(matrizA,matrizB)
    return matrizResultado