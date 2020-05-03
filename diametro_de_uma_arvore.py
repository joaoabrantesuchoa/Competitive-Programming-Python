from collections import deque

n = int(input())
grafo = []
for x in range(n+1):
    grafo.append([])

for x in range(n-1):
    a,b = map(int,input().split())
    grafo[a].append(b)
    grafo[b].append(a)

def bfs(grafo,s):
    q = deque()
    dist = []
    for inf in range(n+5):
        dist.append(-1)
    q.insert(0,s)
    dist[s] = 0
    distance = -1
    global maior 
    maior = 0
    while len(q) != 0:
        popado = q.pop()
        distance += 1
        for adj in grafo[popado]:
            if dist[adj] == -1:
                q.insert(0,adj)
                dist[adj] = dist[popado] + 1
        maior = popado
    return dist


bfs(grafo,1)
caminhos = bfs(grafo,maior)
maxdis = 0

for i in range(len(caminhos)):
    if caminhos[i] > maxdis:
        maxdis = caminhos[i]


print(maxdis)
