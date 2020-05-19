#Lembrando que o grafo não pode ter cíclo e deve ser direcionado
n,m = map(int,input().split())

grafo = [[] for i in range(n)]

visitados = [-1] * n
resp = []

for x in range(m):
    a,b = map(int,input().split())
    grafo[a-1].append(b)

def dfs(v):
    visitados[v-1] = 0

    for adj in grafo[v-1]:
        if visitados[adj-1] == -1:
            dfs(adj)

    resp.append(v)

def topological_sort():
    for i in range(n):
        if visitados[i] == -1:
            dfs(i)
    return resp[::-1]

print(topological_sort())
