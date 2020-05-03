from heapq import *
INF = 1e16
     
n, m = map(int, input().split())
grafo = [[] for _ in range(n)]
distancia = [0] + [INF] * n
vertice_anterior = [-1] * n
q = [(0, 0)]
for i in range(m):
    a, b, w = map(int, input().split())
    grafo[a-1] += [(w, b-1)]
    grafo[b-1] += [(w, a-1)]
while q:
    a = heappop(q)[1]
    for adj in grafo[a]:
    		w, b = distancia[a] + adj[0], adj[1]
    		if w < distancia[b]:
    			distancia[b], vertice_anterior[b] = w, a
    			heappush(q, (distancia[b], b))
if distancia[n-1] == INF:
    print(-1);
else:
    x, y = n - 1, []
    while x != -1:
    	    y += [x + 1]
    	    x = vertice_anterior[x]
    y.reverse()
    print(' '.join(map(str, y)))
