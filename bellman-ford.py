#------COMPLEXIDADE-------
#O(VE) V == vértices e E == arestas


#Naive implementation

INF = 1e12

n,m = map(int,input().split()) 

e = []

for x in range(m):
    a,b,c = map(int,input().split())
    e.append((a,b,c))

def bellman_ford(v):
    distancia = [INF] * n
    distancia[v] = 0
    for i in range(n-1): #Fase atual. Ele vai percorrer o grafo repetidas vezes para otimizar as distancias
        for j in range(m):# Nó atual
            if distancia[e[j][0]] < INF: #Se a distancia de nó inicial V até o nó atual for menor que infinito.
                #Então a distancia do nó atual até o nó destino será igual ao minimo entre a 
                #distancia do nó atual até o destino e a distancia do nó V até o nó atual 
                # mais a distancia global do nó destino
                #É basicamente um dijsktra + BFS só muda a formatação da lista adjacente 
                distancia[e[j][1]] = min (distancia[e[j][1]], distancia[e[j][0]] + e[j][2])
    return distancia

print(bellman_ford(0))

#Faster implementation
#Basicamente a diferença é que ele manda parar de percorrer quando nenhuma distancia muda
#Já que se nenhuma distancia mudar significa que já encontrou todas as menores distâncias
#A complexidade não muda mas acelerar em good e average cases.

def bellman_ford_otimizado(v):
    distancia = [INF] * n
    distancia[v] = 0

    while True:
        qualquer = False

        for j in range(m):

            if distancia[e[j][0] < INF:
                    if distancia[e[j][1] > distancia[e[j][0]] + e[j][2]:
                        distancia[e[j][1] = disntancia[e[j][0] + e[j][2]
                        qualquer = True

        if qualquer is False:
            return d    
        





