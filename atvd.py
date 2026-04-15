Atividade 3 - Criação de Pacote Matemático em Python

Nesta atividade, você deverá estruturar um pacote contendo funções para manipulação de matrizes. As matrizes devem ser tratadas como listas de listas.

Crie um módulo (matrix.py) que contenha as seguintes funções:

transpor_matriz(matriz)
Regra: Deve transformar as linhas da matriz original em colunas e vice-versa.
Entrada: Uma lista de listas .
Saída: Uma nova lista de listas .
multiplicar_matriz(matriz_a, matriz_b)
Regra: Deve realizar a multiplicação matricial clássica (Linha por Coluna).
Validação: A função deve verificar se o número de colunas de A é igual ao número de linhas de B. Caso contrário, retorne uma mensagem de erro ou None.
Entrada: Duas matrizes (listas de listas).
Saída: Uma matriz resultante da multiplicação.
Exemplo de Entrada e Saída Esperada

Crie um arquivo main.py que faça uso do módulo matrix.py e execute os exemplos abaixo.

Transposição

Entrada:

A = [[1, 2], [3, 4], [5, 6]]
Saída:

[[1, 3, 5], [2, 4, 6]]
Multiplicação

Entrada:

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
Saída: (Cálculo: 1*5 + 2*7 = 19, etc.)

[[19, 22], [43, 50]]