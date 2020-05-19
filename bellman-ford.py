#------COMPLEXIDADE-------
#O(VE) V == vértices e E == arestas


#Naive implementation
'''
INF = 1e12

n,m = map(int,input().split()) 

e = []

for x in range(m):
    a,b,c = map(int,input().split())
    e.append((a,b,c))

def bellman_ford(v):
    distancia = [INF] * n
    distancia[v] = 0
    for i in range(n-1):
        for j in range(m):
            if distancia[e[j][0]] < INF:
                distancia[e[j][1]] = min (distancia[e[j][1]], distancia[e[j][0]] + e[j][2])
    return distancia

print(bellman_ford(0))
'''

#Faster implementation
#Basicamente a diferença é que ele manda parar de percorrer quando nenhuma distancia muda
#Já que se nenhuma distancia mudar significa que já encontrou todas as menores distâncias
#A complexidade não muda mas acelerar em good e average cases.
'''
INF = 1e12

n,m = map(int,input().split())

e = []

for x in range(m):
    a,b,c = map(int,input().split())
    e.append((a,b,c))

def bellman_ford(v):
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
        

print(bellman_ford(0))

'''
#Printar o caminho percorrido para achar a menor distância entre dois vértices






