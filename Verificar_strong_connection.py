'''
Um grafo fortemente conectado consiste na possibilidade de existir um caminho de qualquer vértice para qualquer outro. 
'''

respostas = []

def adicionar_no(grafo_reverso, origem, destino):
    grafo_reverso[origem - 1].append(destino + 1)
    #grafo_reverso[origem].append(destino) para caso o primeiro vértice ser 0.

def transpor_grafo(grafo , grafo_reverso, n):
    for i in range(n):
        for j in range(len(grafo[i])):
            adicionar_no(grafo_reverso, grafo[i][j], i)
    return grafo_reverso

def dfs(i,grafo,visitados):
    visitados[i-1] = True
    for adj in grafo[i-1]:
        if visitados[adj-1] == False:
            visitados[adj-1] = True
            dfs(adj,grafo,visitados)
    return visitados

while True:
    n,m = map(int,input().split())

    grafo = [[] for i in range(2001)]
    visitados = [False] * n
    if n == 0 and m == 0:
        break

    for x in range(m):
        a,b,w = map(int,input().split())

        if w == 1: #Se w for 1 a aresta é direcionada
            grafo[a-1].append(b)
        elif w == 2: # Se w for 0 a aresta não é direcionada
            grafo[a-1].append(b)
            grafo[b-1].append(a)


    dfs(1,grafo,visitados)

    if visitados.count(True) != n:
       respostas.append(0)

    else:
        visitados = [False] * n

        grafo_reverso = [[] for i in range(2001)]
        transpor_grafo(grafo, grafo_reverso, n)


        dfs(1,grafo_reverso,visitados)

        if visitados.count(True) == n:
            respostas.append(1)
        else:
            respostas.append(0)


for x in respostas:
    print(x)
