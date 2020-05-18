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
        z,a = heappop(q)
        if a == v: #Implementação para quando vocẽ quer a distancia entre dois nós
        #Se você já chegou nele com a menor distância não precisa percorrer o resto do grafo.
             return distancia[v]
        else:
            if z <= distancia[a]:#Implementação para acelerar a comparação de distância e ignorar
            #Alguns nó inutéis, já que você não precisa comparar nós que tem uma distância maior que a atual
            #não faz mt sentido você visitá-los sendo que já sabe uma distância menor.
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
