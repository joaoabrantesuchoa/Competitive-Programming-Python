#BFS de um grafo não ponderado e não direcionado
from collections import deque

n,m = map(int,input().split())

grafo = [[] for i in range(n)]

distancia = [0] * n
caminho_percorrido = [0] * n
visitados = [0] * n

for i in range(m):
    a,b = map(int,input().split())
    grafo[a-1].append(b)
    grafo[b-1].append(a)


def bfs_zerada(v):
    q = deque()
    q.append(v)
    visitados[v-1] = 1
    while q:
        popado = q.popleft()
        for adj in grafo[popado - 1]:
            if visitados[adj-1] == 0:
                visitados[adj-1] = 1
                q.append(adj)

    return visitados

def bfs_distancia(v):
    q = deque()
    q.append(v)
    visitados[v-1] = 1
    while q:
        popado = q.popleft()
        for adj in grafo[popado - 1]:
            if visitados[adj-1] == 0:
                visitados[adj-1] = 1
                distancia[adj-1] = distancia[popado-1] + 1
                q.append(adj)
    print(visitados)
    print(distancia)

#Também pode ajeitar a BFS para ela percorrer entre dois nós
#No caso se o popado for o nó desejado E a BFS para.
#Esse caso é útil para quando você tem que encontrar a menor
#distância entre dois nós em uma grafo não ponderado, pois
#desse modo, você não precisa percorrer ele todo.

#Para mostrar o caminho percorrido obviamente você tem que usar a parte de parar quando achar o vértice
#destino

# O código abaixo tá errado, lembrar de ajeitar dps
def bfs_entre_dois_nos(v,u):
    q = deque()
    q.append(v)
    visitados[v-1] = 1
    caminho_percorrido[v-1] = -1
    while q:
        popado = q.popleft()
        for adj in grafo[popado - 1]:
            if adj == u:
                if visitados[adj-1] == 0:
                    visitados[adj-1] = 1
                    distancia[adj-1] = distancia[popado - 1] + 1
                    caminho_percorrido[adj-1] = popado
                mostrar_caminho_percorrido(caminho_percorrido,visitados,v,u)
            else:
                if visitados[adj-1] == 0:
                    visitados[adj-1] = 1
                    distancia[adj-1] = distancia[popado-1] + 1
                    caminho_percorrido[adj-1] = popado
                    q.append(adj)
    mostrar_caminho_percorrido(caminho_percorrido,visitados,v,u)


def mostrar_caminho_percorrido(caminho_percorrido,visitados,v,u):#Caminho entre a origem(V) e o vértice U.
    print(caminho_percorrido)
    if visitados[u-1] == 0:
        print("NO PATH")
    else:
        v = u
        path = []
        while v != -1:
            v = caminho_percorrido[v-1]
            path.append(v)
        path = path.reverse()
        for i in path:
            print(v , end = " ")

