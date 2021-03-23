# Inicializa a matriz
nLinha = 3  # Numero de Linhas da Matriz
nColuna = 3  # Numero de Coluna da Matriz
matrix = [] # Cria a Matriz

# Inicializa os valores da matriz
print("ENTRE COM OS VALORES (EM ORDEM DE LINHA): ")
for i in range(nLinha):  # Loop para a entrada das linhas
    a = []
    for j in range(nColuna):  # Loop para a entrada das colunas
        a.append(int(input()))
    matrix.append(a)

# Realiza os calculos
calculoPositivo = ((matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[0][1]
                   * matrix[1][2] * matrix[2][0]) + (matrix[0][2] * matrix[1][0] * matrix[2][1]))

calculoNegativo = ((- matrix[0][2] * matrix[1][1] * matrix[2][0]) - (matrix[0][0]
                   * matrix[1][2] * matrix[2][1]) - (matrix[0][1] * matrix[1][0] * matrix[2][2]))

calculoDeterminante = (calculoPositivo) - (-calculoNegativo)

# Imprime msg
print("\n\nA MATRIZ FICOU: ")
# Imprime a Matriz
for i in range(nLinha):
    for j in range(nColuna):
        print(matrix[i][j], end=" \t ")
    print()
# Imprime o resultado os calculos
print("CALCULO POSITIVO: ", calculoPositivo)
print("CALCULO NEGATIVO: ", calculoNegativo)
print("CALCULO DETERMINANTE: ",  calculoDeterminante)
