from heapq import *
INF = 1e16
N,M = map(int,input().split())

lista_adjacente = [[] for i in range(N+1)]

for i in range(M):
    a,b,w = map(int,input().split())
    lista_adjacente[a] += [(w,b)]
    lista_adjacente[b] += [(w,a)]

def dijsktra(u,v,lista_adjacente):
    distancia[u] = 0
    q = [(0,u)]
    while q:
        a = heappop(q)[1]
        for adj in lista_adjacente[a]:
            w,b = distancia[a] + adj[0],adj[1]
            if w < distancia[b]:
                distancia[b] = w
                heappush(q,(distancia[b],b))
    return distancia[v]


distancia = [INF] * (N+1)
distancias_ao_destino = []
u,v = map(int,input().split())

dist_u_v = dijsktra(u,v,lista_adjacente)

if dist_u_v == INF:
    print("NO PATH")
else:
    print(dist_u_v)
