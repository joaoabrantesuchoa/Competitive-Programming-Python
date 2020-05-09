n,m = map(int,input().split())

def dfs(v):
    visitados[v] = 0

    for adj in grafo[v]:
        if visitados[adj] == -1:
            visitados[adj] = 0
            dfs(adj)


grafo = [[] for i in range(n+1)]
visitados = [-1] * (n + 1)


for x in range(m):
    a,b = map(int,input().split())
    grafo[a].append(b)
    grafo[b].append(a)

dfs(1)
print(visitados)
