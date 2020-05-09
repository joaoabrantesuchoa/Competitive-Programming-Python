from queue import Queue

n,m = map(int,input().split())


grafo = [[] for i in range(n+1)]
visitados = [0] * (n + 1)

for i in range(m):
    a,b = map(int,input().split())
    grafo[a].append(b)
    grafo[b].append(a)

def bfs(v):
    q = Queue(maxsize = n)
    q.put(v)
    visitados[v] = 1
    while not q.empty():
        popado = q.get()
        for adj in grafo[popado]:
            if visitados[adj] == 0:
                visitados[adj] = 1
                q.put(v)
    return visitados

bfs(1)
print(visitados)
